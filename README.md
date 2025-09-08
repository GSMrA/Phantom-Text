README - Cryptage/Décryptage de messages
Description

Ce projet propose un programme Python pour crypter et décrypter des messages avec une clé personnalisée.
Il existe deux versions :

Version console : fonctionne entièrement dans le terminal.

Version GUI (interface graphique) : utilise Tkinter pour une interface plus conviviale et interactive.

Les deux versions incluent :

Génération de clé unique (254 caractères)

Vérification de la clé (longueur et absence de doublons)

Cryptage et décryptage de messages

Option d’envoi par email des clés ou des messages cryptés/décryptés

Version console
Fonctionnalités

Menu interactif avec choix de l’action :

Générer une clé

Crypter un message

Décrypter un message

Quitter

Horodatage de chaque étape (TIME : xxxx || …)

Vérification automatique de la clé

Envoi par email possible pour les clés et résultats

Installation

Installer Python 3.x

Installer les modules requis (smtplib et email sont intégrés à Python, pas besoin d’installer)

Utilisation

Lancer le script python cryptage_console.py

Suivre les instructions dans le menu :

Générer une clé

Entrer la clé et le message à crypter/décrypter

Optionnel : envoyer le résultat par email

Version GUI (interface graphique)
Fonctionnalités

Interface conviviale avec Tkinter

Champs pour saisir le texte et la clé

Boutons pour :

Générer une clé

Crypter un message

Décrypter un message

Zone de résultats avec horodatage (TIME : xxxx || …)

Option d’envoi par email

Vérification de la clé avant chaque action

Installation

Installer Python 3.x

Installer Tkinter (inclus généralement avec Python sur Windows/Mac)

Aucun module externe supplémentaire requis

Utilisation

Lancer le script python cryptage_gui.py

Saisir le texte et la clé

Cliquer sur les boutons correspondants pour générer la clé, crypter ou décrypter

Voir le résultat dans la zone “Résultat” avec horodatage

Optionnel : envoyer par email directement depuis l’application

Remarques de sécurité

L’envoi d’emails utilise SMTP Gmail. Vous devez autoriser les applications moins sécurisées ou générer un mot de passe spécifique pour l’application.

La clé générée est essentielle pour déchiffrer un message, ne la perdez pas !

Les messages cryptés ne sont sécurisés que par ce système de substitution, ce n’est pas du chiffrement cryptographique avancé.

Auteurs

Créé par Mahé

Version console et GUI maintenues par l’auteur
