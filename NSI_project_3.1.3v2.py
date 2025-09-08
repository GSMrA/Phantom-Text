import tkinter as tk
from tkinter import messagebox, simpledialog
from random import randint
from time import monotonic, sleep
import smtplib
from email.mime.text import MIMEText

# Liste des caractères
ressources_caractères = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "à","â","ä","ç","é","è","ê","ë","î","ï","ô","ö","ù","û","ü","ÿ","œ","æ",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "À","Â","Ä","Ç","É","È","Ê","Ë","Î","Ï","Ô","Ö","Ù","Û","Ü","Ÿ","Œ","Æ",
    "0","1","2","3","4","5","6","7","8","9",
    ".","…",",",";","!","?",":","'","-","_","{","}","/",
    "@","#","$","%","&","*","+","=","~","^","`","<",">",
    " ","(",")"
]

# --- FONCTION D'AFFICHAGE HORODATÉ DANS LE RESULTAT ---
def add_time_message(message):
    t = str(int(round(monotonic(),0)))
    entry_result.insert(tk.END, f"TIME : {t} || {message}\n")
    entry_result.see(tk.END)

# --- FONCTIONS DE CLÉ ---
def generate_small_key():
    caractères = list(ressources_caractères)
    key = []
    for i in range(len(caractères)):
        c = randint(0,len(caractères)-1)
        key.append(caractères[c])
        del caractères[c]
    return "".join(key)

def generate_key():
    key1 = generate_small_key()
    key2 = generate_small_key()
    key_drop = key1 + key2
    entry_key.delete(0, tk.END)
    entry_key.insert(0, key_drop)
    add_time_message("Clé générée !")

    if messagebox.askyesno("Envoyer par email", "Voulez-vous envoyer la clé par email ?"):
        dest = simpledialog.askstring("Email", "Adresse email du destinataire :")
        if dest:
            send_email(dest, "Votre clé secrète", f"Voici votre clé :\n{key_drop}")

# --- FONCTION D'ENVOI EMAIL ---
def send_email(destinataire, subject, contenu):
    expediteur = "gs.dev.mra@gmail.com"
    mdp = "xodu xxti alvq lhup"
    serveur_smtp = "smtp.gmail.com"
    port_smtp = 587

    message = MIMEText(contenu)
    message["Subject"] = subject
    message["From"] = expediteur
    message["To"] = destinataire

    try:
        with smtplib.SMTP(serveur_smtp, port_smtp) as server:
            server.starttls()
            server.login(expediteur, mdp)
            server.sendmail(expediteur, destinataire, message.as_string())
        add_time_message("Email envoyé avec succès !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'envoi : {e}")

# --- FONCTION DE VÉRIFICATION DE CLÉ ---
def verify_key(recup_key):
    if len(recup_key) != 254:
        messagebox.showerror("Erreur", "La clé doit contenir 254 caractères !")
        return None, None
    
    key1_list = [recup_key[i] for i in range(127)]
    key2_list = [recup_key[i] for i in range(127,254)]
    
    for c in key1_list:
        if key2_list.count(c) != 1:
            messagebox.showerror("Erreur", f"Erreur de clé, caractère dupliqué : {c}")
            return None, None
    add_time_message("Clé vérifiée avec succès")
    return key1_list, key2_list

# --- CRYPTER ---
def crypter():
    text = entry_text.get("1.0", tk.END).strip()
    recup_key = entry_key.get().strip()

    add_time_message("Vérification de la clé pour le cryptage...")
    key1_list, key2_list = verify_key(recup_key)
    if not key1_list:
        return

    add_time_message("Cryptage en cours...")
    try:
        crypted_text = "".join([key1_list[key2_list.index(c)] for c in text])
    except ValueError as e:
        messagebox.showerror("Erreur", f"Caractère non reconnu : {e}")
        return

    entry_result.insert(tk.END, f"TIME : {int(round(monotonic(),0))} || Texte crypté : {crypted_text}\n")

    if messagebox.askyesno("Envoyer par email", "Voulez-vous envoyer le texte crypté par email ?"):
        dest = simpledialog.askstring("Email", "Adresse email du destinataire :")
        if dest:
            contenu = f"""Clé utilisée :\n{recup_key}\n\nTexte original :\n{text}\n\nTexte crypté :\n{crypted_text}"""
            send_email(dest, "Résultat du cryptage", contenu)

# --- DÉCRYPTER ---
def décrypter():
    text = entry_text.get("1.0", tk.END).strip()
    recup_key = entry_key.get().strip()

    add_time_message("Vérification de la clé pour le décryptage...")
    key1_list, key2_list = verify_key(recup_key)
    if not key1_list:
        return

    add_time_message("Décryptage en cours...")
    try:
        uncrypted_text = "".join([key2_list[key1_list.index(c)] for c in text])
    except ValueError as e:
        messagebox.showerror("Erreur", f"Caractère non reconnu : {e}")
        return

    entry_result.insert(tk.END, f"TIME : {int(round(monotonic(),0))} || Texte décrypté : {uncrypted_text}\n")

    if messagebox.askyesno("Envoyer par email", "Voulez-vous envoyer le texte décrypté par email ?"):
        dest = simpledialog.askstring("Email", "Adresse email du destinataire :")
        if dest:
            contenu = f"""Clé utilisée :\n{recup_key}\n\nTexte crypté :\n{text}\n\nTexte décrypté :\n{uncrypted_text}"""
            send_email(dest, "Résultat du décryptage", contenu)

# --- INTERFACE ---
root = tk.Tk()
root.title("Cryptage/Décryptage avec TIME")
root.geometry("800x600")

tk.Label(root, text="Texte à crypter/décrypter :").pack()
entry_text = tk.Text(root, height=8)
entry_text.pack()

tk.Label(root, text="Clé (254 caractères) :").pack()
entry_key = tk.Entry(root, width=100)
entry_key.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Générer clé", width=15, command=generate_key).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="🔒 Crypter", width=15, command=crypter).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="🔓 Décrypter", width=15, command=décrypter).grid(row=0, column=2, padx=5)

tk.Label(root, text="Résultat :").pack()
entry_result = tk.Text(root, height=10)
entry_result.pack()

root.mainloop()
