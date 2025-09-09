from math import *  # Importe toutes les fonctions mathématiques (sqrt, sin, etc.)
from random import *  # Importe toutes les fonctions de génération aléatoire
from time import *  # Importe les fonctions liées au temps (sleep, monotonic, etc.)
import sys  # Importe le module système
from sys import *  # Importe toutes les fonctions du module système
import os  # Importe les fonctions pour interagir avec le système d’exploitation
from os import *  # Importe tout depuis le module os
import io  # Importe les fonctions d’entrée/sortie
import smtplib  # Module pour envoyer des emails via SMTP
from email.mime.text import MIMEText  # Permet de créer des emails au format texte

ressources_caractères = [  # Liste de tous les caractères utilisables pour le chiffrement
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "à","â","ä","ç","é","è","ê","ë","î","ï","ô","ö","ù","û","ü","ÿ","œ","æ",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "À","Â","Ä","Ç","É","È","Ê","Ë","Î","Ï","Ô","Ö","Ù","Û","Ü","Ÿ","Œ","Æ",
    "0","1","2","3","4","5","6","7","8","9",
    ".","…",",",";","!","?",":","'","-","_","{","}","/",
    "@","#","$","%","&","*","+","=","~","^","`","<",">",
    " ","(",")"
]

def generate_small_key():  # Fonction pour générer une moitié de la clé de chiffrement
    caractères = list(ressources_caractères)  # Copie la liste des caractères
    key = []  # Initialise la clé vide
    for i in range(len(caractères)):  # Pour chaque caractère possible
        caractere_choisi = randint(0,len(caractères)-1)  # Prend un caractère aléatoire
        key.append(caractères[caractere_choisi])  # L’ajoute à la clé
        del caractères[caractere_choisi]  # Le supprime de la liste pour éviter les doublons
    key_text = ""  # Initialise la clé finale sous forme de chaîne
    for i in range(len(key)):  # Convertit la liste en chaîne
        key_text += key[i]
    return key_text  # Retourne la clé générée

def generate_key():  # Fonction principale de génération de clé
    key1 = generate_small_key()  # Génère la première moitié de la clé
    key2 = generate_small_key()  # Génère la deuxième moitié de la clé
    key_drop = key1 + key2  # Combine les deux moitiés
    print(key_drop)  # Affiche la clé complète

    send_mail = input("Voulez-vous envoyer la clé par email ? (oui/non) : ").lower()  # Demande si on veut envoyer la clé par mail

    if send_mail == "oui":  # Si l'utilisateur accepte
        cible = input("Entrez l'adresse email du destinataire : ")  # Demande l'adresse de destination

        expediteur = "gs.dev.mra@gmail.com"  # Email de l'expéditeur
        mdp = "xodu xxti alvq lhup"  # Mot de passe de l'expéditeur (mot de passe d’application)
        serveur_smtp = "smtp.gmail.com"  # Adresse SMTP
        port_smtp = 587  # Port SMTP utilisé

        message = MIMEText(f"Voici votre clé :\n {key_drop}")  # Création du message texte
        message["Subject"] = "Votre clé secrète"  # Sujet de l’email
        message["From"] = expediteur  # Adresse de l'expéditeur
        message["To"] = cible  # Adresse du destinataire

        try:  # Essaye d'envoyer le mail
            with smtplib.SMTP(serveur_smtp, port_smtp) as server:  # Connexion au serveur
                server.starttls()  # Démarre le mode sécurisé
                server.login(expediteur, mdp)  # Connexion avec le mot de passe
                server.sendmail(expediteur, cible, message.as_string())  # Envoi du mail
            print("Email envoyé avec succès !")  # Succès
        except Exception as e:  # En cas d'erreur
            print("Erreur lors de l'envoi :", e)  # Affiche l’erreur

    else:  # Si l’utilisateur refuse l’envoi
        print("Envoi annulé.")  # Message d’annulation

def recup_key(recup_key):  # Fonction pour séparer une clé en deux listes (inutile ici, jamais appelée correctement)
    key1_list = []  # Liste de la première moitié de la clé
    key2_list = []  # Liste de la deuxième moitié de la clé
    for i in range (127):  # Première moitié
        key1_list.append(recup_key[i])
    for i in range(254,254):  # Mauvaise plage (aucun caractère ici)
        key2_list.append(recup_key[i])
    return key1_list, key2_list  # Retourne les deux moitiés

def crypter():  # Fonction de cryptage
    time = str(int(round(monotonic(),0)))  # Récupère l'heure en secondes
    textmessage = "TIME : "+ time + "||Entrez le texte a crypter : \n"  # Prépare le message
    text = str(input(textmessage))  # Demande le texte à crypter
    
    time = str(int(round(monotonic(),0)))  # Heure actuelle
    textmessage ="TIME : "+ time + "||Entrez la clef de Cryptage : \n"  # Message pour demander la clé
    recup_key = str(input(textmessage))  # Récupère la clé

    time = str(int(round(monotonic(),0)))  # Heure actuelle
    print("TIME : ",time,"||Vérification de la Clef de Cryptage")  # Message de vérification
    time = str(int(round(monotonic(),0)))  # Heure
    sleep(2)  # Pause de 2 secondes
    
    print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : En Cours")  # Vérification longueur
    time = str(int(round(monotonic(),0)))  # Heure
    if len(recup_key)!=254:  # Si la clé n’a pas la bonne longueur
        print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : Erreur")  # Erreur
        return  # Arrête la fonction
    
    else:
        print("TIME : ",time,"||Vérification de la longeur de la clef || Statut : Fait")  # Longueur correcte
    print("TIME : ",time,"||Vérification de la presence de chaque caractère || Statut : En Cours")  # Vérification du contenu
    sleep(1.5)  # Pause

    key1_list = []  # Liste de correspondance
    key2_list = []  # Liste d’ordre
    for i in range (127):  # Première moitié
        key1_list.append(recup_key[i])
    for i in range(127,254):  # Deuxième moitié
        key2_list.append(recup_key[i])
    
    caractères = list(ressources_caractères)  # Copie des caractères disponibles
    for i in range(127):  # Vérifie que chaque caractère apparaît une fois
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

    text_list = []  # Texte sous forme de liste
    crypted_text = []  # Texte crypté sous forme de liste
    crypted_text_output = ""  # Texte final crypté
    for i in range (len(text)):  # Conversion texte en liste
        text_list.append(text[i])
    for i in range (len(text)):  # Pour chaque caractère
        crypted_text.append(key1_list[key2_list.index(text[i])])  # Remplace selon clé

    for i in range(len(crypted_text)):  # Transforme la liste en texte final
        crypted_text_output = crypted_text_output + crypted_text[i]
        
    time = str(int(round(monotonic(),0)))
    print("TIME : ",time,"||Voici votre texte crypté :\n\n")
    print(crypted_text_output)

    envoyer_mail = input("\nVoulez-vous envoyer le résultat par email ? (oui/non) : ").lower()  # Propose d’envoyer le message

    if envoyer_mail == "oui":
        destinataire = input("Entrez l'adresse email du destinataire : ")  # Adresse destinataire

        expediteur = "gs.dev.mra@gmail.com"
        mdp = "xodu xxti alvq lhup"
        serveur_smtp = "smtp.gmail.com"
        port_smtp = 587

        contenu = f"""  # Corps du message email
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

