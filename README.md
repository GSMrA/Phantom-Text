# Cryptage/Décryptage de messages

## Description

Ce projet propose un programme Python pour **crypter et décrypter des messages** avec une clé personnalisée.  

Il existe **deux versions** :  

1. **Version console** : fonctionne entièrement dans le terminal.  
2. **Version GUI (interface graphique)** : utilise Tkinter pour une interface plus conviviale et interactive.  

Les deux versions incluent :  
- Génération de clé unique (254 caractères)  
- Vérification de la clé (longueur et absence de doublons)  
- Cryptage et décryptage de messages  
- Option d’envoi par email des clés ou des messages cryptés/décryptés  

---

## Version console

### Fonctionnalités
- Menu interactif avec choix de l’action :  
  - Générer une clé  
  - Crypter un message  
  - Décrypter un message  
  - Quitter  
- Horodatage de chaque étape (`TIME : xxxx || …`)  
- Vérification automatique de la clé  
- Envoi par email possible pour les clés et résultats  

### Installation
1. Installer Python 3.x  
2. Installer les modules requis (smtplib et email sont intégrés à Python)  

### Utilisation
1. Lancer le script :  
```bash
python cryptage_console.py
