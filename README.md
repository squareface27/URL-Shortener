# URL Shortener

## Description

Ce projet, "URL Shortener", est un outil permettant de raccourcir les URLs en utilisant l'API de Bitly. Il est doté d'une interface utilisateur graphique simple et intuitive pour faciliter son utilisation.

## Fonctionnalités

- Raccourcissement des URLs en utilisant l'API de Bitly.
- Interface utilisateur graphique pour une utilisation facile.
- Support multilingue (Français et Anglais).

## Technologies Utilisées

- Python
- API de Bitly

## Installation et Configuration

1. **Clonage du Répertoire** : Clonez ce répertoire sur votre machine.

   ```bash
   git clone https://github.com/squareface27/URL-Shortener.git
   cd URL-Shortener
   ```

2. **Installation des Dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration des Variables d'Environnements** : Renommez le fichier `.env.example` en `.env` et ajoutez-y votre token Bitly et le group GUID :
   ```bash
   TOKEN=your_bitly_token
   GROUP_GUID=your_group_guid
   ```

## Utilisation du programme

1. **Choix de la Langue** : Par défaut, l'application est en anglais. Vous pouvez changer la langue en modifiant la variable language dans le fichier `main.py` ('en' pour anglais, 'fr' pour français).

<br>

2. **Raccourcissement d'URL** :

- Entrez l'URL à raccourcir dans le champ prévu.
- Cliquez sur le bouton "Soumettre".
- L'URL raccourcie sera copiée automatiquement dans votre presse-papiers.

![image](https://images.squareface.fr/projets/UrlShortener/image.png)
