from math import *
from random import *
from time import *
import sys
from sys import *
import os
from os import *
import io
import smtplib
from email.mime.text import MIMEText


# Génération de la clé de chiffrement
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

def generate_small_key():
    caractères = list(ressources_caractères)
    key = []
    for i in range(len(caractères)):
        caractere_choisi = randint(0,len(caractères)-1)
        key.append(caractères[caractere_choisi])
        del caractères[caractere_choisi]
    key_text = ""
    for i in range(len(key)):
        key_text += key[i]
    return key_text
def generate_key():
    key1 = generate_small_key()
    key2 = generate_small_key()
    key_drop = key1 + key2
    print(key_drop)



    # On demande si on veut envoyer par mail
    send_mail = input("Voulez-vous envoyer la clé par email ? (oui/non) : ").lower()

    if send_mail == "oui":
        cible = input("Entrez l'adresse email du destinataire : ")

        # --- CONFIGURATION ---
        expediteur = "gs.dev.mra@gmail.com"
        mdp = "xodu xxti alvq lhup"
        serveur_smtp = "smtp.gmail.com"
        port_smtp = 587
        # ------------------------------------------------

        # Création du message
        message = MIMEText(f"Voici votre clé :\n {key_drop}")
        message["Subject"] = "Votre clé secrète"
        message["From"] = expediteur
        message["To"] = cible

        try:
            with smtplib.SMTP(serveur_smtp, port_smtp) as server:
                server.starttls()
                server.login(expediteur, mdp)
                server.sendmail(expediteur, cible, message.as_string())
            print("Email envoyé avec succès !")
        except Exception as e:
            print("Erreur lors de l'envoi :", e)

    else:
        print("Envoi annulé.")





    




#Récuperer la clé de chiffrement
def recup_key(recup_key):
    #recup_key = str(input("Entrez la clé de chiffrement : "))
    key1_list = []
    key2_list = []
    for i in range (127):
        key1_list.append(recup_key[i])
    for i in range(254,254):
        key2_list.append(recup_key[i])
    return key1_list, key2_list
def crypter():
    time = str(int(round(monotonic(),0)))
    textmessage = "TIME : "+ time + "||Entrez le texte a crypter : \n"
    text = str(input(textmessage))
    
    time = str(int(round(monotonic(),0)))
    textmessage ="TIME : "+ time + "||Entrez la clef de Cryptage : \n"
    recup_key = str(input(textmessage))

    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Vérification de la Clef de Cryptage")
    time = str(int(round(monotonic(),0)))
    sleep(2)
    
    print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : En Cours")
    time = str(int(round(monotonic(),0)))
    if len(recup_key)!=254:
        print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : Erreur")
        return
    
    else:
        print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : Fait")
    print("TIME : ",time,"||Vérification de la presence de chaque caractère || Statut : En Cours")
    sleep(1.5)

    key1_list = []
    key2_list = []
    for i in range (127):
        key1_list.append(recup_key[i])
    for i in range(127,254):
        key2_list.append(recup_key[i])
    

    #key 2 c lordre des caractères
    

    caractères = list(ressources_caractères)
    for i in range(127):
        if key2_list.count(key1_list[i]) == 1:
            print("TIME : ",time,"||Caractère '",key1_list[i],"' Vérifié")
            time = str(int(round(monotonic(),0)))
        else:
            print("\nTIME : ",time,"||Caractère '",key1_list[i],"' Erreur")
            return
    print("TIME : ",time,"||Vérification de la presence de chaque caractère || Statut : Fait\n")
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||La Clef a bien été vérifiée")
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Cryptage en cours\n")

    text_list = []
    crypted_text = []
    crypted_text_output = ""
    for i in range (len(text)):
        text_list.append(text[i])
    for i in range (len(text)):
        crypted_text.append(key1_list[key2_list.index(text[i])])

    for i in range(len(crypted_text)):
        crypted_text_output = crypted_text_output + crypted_text[i]
        
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Voici votre texte crypté :\n\n")

    print(crypted_text_output)



        # --- Envoi par email ---


    envoyer_mail = input("\nVoulez-vous envoyer le résultat par email ? (oui/non) : ").lower()

    if envoyer_mail == "oui":
        destinataire = input("Entrez l'adresse email du destinataire : ")

        expediteur = "gs.dev.mra@gmail.com"
        mdp = "xodu xxti alvq lhup"  
        serveur_smtp = "smtp.gmail.com"
        port_smtp = 587

        # Création du message
        contenu = f"""
        **Clé utilisée :
        {recup_key}

        **Texte original :
        {text}

        **Texte crypté :
        {crypted_text_output}
        """
        message = MIMEText(contenu)
        message["Subject"] = "Résultat du cryptage"
        message["From"] = expediteur
        message["To"] = destinataire

        try:
            with smtplib.SMTP(serveur_smtp, port_smtp) as server:
                server.starttls()
                server.login(expediteur, mdp)
                server.sendmail(expediteur, destinataire, message.as_string())
            print(" Email envoyé avec succès !")
        except Exception as e:
            print(" Erreur lors de l'envoi :", e)









    



def décrypter():
    time = str(int(round(monotonic(),0)))
    textmessage = "TIME : "+ time + "||Entrez le texte a décrypter : \n"
    text = str(input(textmessage))
    
    time = str(int(round(monotonic(),0)))
    textmessage ="TIME : "+ time + "||Entrez la clef de Décryptage : \n"
    recup_key = str(input(textmessage))

    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Vérification de la Clef de Décryptage")
    time = str(int(round(monotonic(),0)))
    sleep(2)
    
    print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : En Cours")
    time = str(int(round(monotonic(),0)))
    if len(recup_key)!=254:
        print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : Erreur")
        return
    
    else:
        print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : Fait")
    print("TIME : ",time,"||Vérification de la presence de chaque caractère || Statut : En Cours")
    sleep(1.5)

    key1_list = []
    key2_list = []
    for i in range (127):
        key1_list.append(recup_key[i])
    for i in range(127,254):
        key2_list.append(recup_key[i])
    

    #key 2 c lordre des caractères
    

    caractères = list(ressources_caractères)
    for i in range(127):
        if key2_list.count(key1_list[i]) == 1:
            print("TIME : ",time,"||Caractère '",key1_list[i],"' Vérifié")
            time = str(int(round(monotonic(),0)))
        else:
            print("\nTIME : ",time,"||Caractère '",key1_list[i],"' Erreur")
            return
    print("TIME : ",time,"||Vérification de la presence de chaque caractère || Statut : Fait\n")
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||La Clef a bien été vérifiée")
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Décryptage en cours\n")

    text_list = []
    uncrypted_text = []
    uncrypted_text_output = ""
    for i in range (len(text)):
        text_list.append(text[i])
    for i in range (len(text)):
        uncrypted_text.append(key2_list[key1_list.index(text_list[i])])

    for i in range(len(uncrypted_text)):
        uncrypted_text_output = uncrypted_text_output + uncrypted_text[i]
        
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Voici votre texte décrypté :\n\n")

    print(uncrypted_text_output)
    



        # --- Envoi par email ---


    envoyer_mail = input("\nVoulez-vous envoyer le résultat par email ? (oui/non) : ").lower()

    if envoyer_mail == "oui":
        destinataire = input("Entrez l'adresse email du destinataire : ")

        expediteur = "gs.dev.mra@gmail.com"
        mdp = "xodu xxti alvq lhup"  #
        serveur_smtp = "smtp.gmail.com"
        port_smtp = 587

        # Création du message
        contenu = f"""
        **Clé utilisée :
        {recup_key}

        **Texte crypté (fourni en entrée) :
        {text}

        **Texte décrypté :
        {uncrypted_text_output}
        """
        message = MIMEText(contenu)
        message["Subject"] = "Résultat du décryptage"
        message["From"] = expediteur
        message["To"] = destinataire

        try:
            with smtplib.SMTP(serveur_smtp, port_smtp) as server:
                server.starttls()
                server.login(expediteur, mdp)
                server.sendmail(expediteur, destinataire, message.as_string())
            print(" Email envoyé avec succès !")
        except Exception as e:
            print(" Erreur lors de l'envoi :", e)

    






def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(

                "\t\t\t\t\t  _____    __    __       ___      .__   __. .___________.  ______   .___  ___.    .___________. __________   ___ .___________.\n"
                "\t\t\t\t\t|   _  \  |  |  |  |     /   \     |  \ |  | |           | /  __  \  |   \/   |    |           ||   ____\  \ /  / |           |\n"
                "\t\t\t\t\t|  |_)  | |  |__|  |    /  ^  \    |   \|  | `---|  |----`|  |  |  | |  \  /  |    `---|  |----`|  |__   \  V  /  `---|  |----`\n"
                "\t\t\t\t\t|   ___/  |   __   |   /  /_\  \   |  . `  |     |  |     |  |  |  | |  |\/|  |        |  |     |   __|   >   <       |  | \n"    
                "\t\t\t\t\t|  |      |  |  |  |  /  _____  \  |  |\   |     |  |     |  `--'  | |  |  |  |        |  |     |  |____ /  .  \      |  |  \n"   
                "\t\t\t\t\t| _|      |__|  |__| /__/     \__\ |__| \__|     |__|      \______/  |__|  |__|        |__|     |_______/__/ \__\     |__|\n"




              )



        
        print("\t\t\t\t\t\t\t\t\t\t\t====================================")
        print("\t\t\t\t\t\t\t\t\t\t\t                MENU                ")
        print("\t\t\t\t\t\t\t\t\t\t\t====================================")
        print("")
        print("\t\t\t\t\t\t\t\t\t\t\t[1] 🔑 Générer une clé")
        print("\t\t\t\t\t\t\t\t\t\t\t[2] 🔒 Crypter un message")
        print("\t\t\t\t\t\t\t\t\t\t\t[3] 🔓 Décrypter un message")
        print("\t\t\t\t\t\t\t\t\t\t\t[0] ❌ Quitter")
        print("")
        choix = input("\t\t\t\t\t\t\t\t\t\t\t👉 Choisis une option : ")
        print("\n\n")

        if choix == "1":
            generate_key()
        elif choix == "2":
            crypter()
        elif choix == "3":
            décrypter()
        elif choix == "0":
            print("\n\t\t\t\t\t\t\t\t\t\t\tBye BYEEEEEE ! 👋")
            break
        else:
            print("\n\t\t\t\t\t\t\t\t\t\t\t[!] Choix invalide")
        
        input("\n\t\t\t\t\t\t\t\t\t\t\tAppuie sur Entrée pour revenir au menu\n")

menu()






    
    
        
    
          
    
    


        
        
    






    
    
    
    
        
        

  

    
    
    
    
        
        

  

