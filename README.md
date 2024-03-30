# PROJET_QR_CODE
## Contenu du projet
### Dossier src :
- seeds_generator.py --> Permet de générer N germes dans les bornes des qrcodes
- qr_generator.py --> Permet de générer le QR code hôte et tous les QR codes qui sont à cacher
- voronoi_qr.py --> Tous les algorithmes du projet
- main.py --> Utilise les fonctions dans voronoi_qr.py pour générer les QR codes augmentés et récupérer les QR codes à cacher

### Dossier qrcodes :
- qrcodes/qrcode_host.png --> QR code hôte qui est utilisé pour toutes les parties du projet
- qrcodes/qrcode_hidden.png --> Le QR code à cacher dans le QR code hôte
- qrcodes/qrcode_augmented.png --> Le QR code hôte avec les informations du QR code à cacher dissimulées à l'intérieur
- qrcodes/qrcode_hidden_retrieved.png --> Le QR code caché qui a été récupéré avec la fonction extract
- Pour les autres dossiers (multiples & secured) il s'agit de la même chose pour les parties 2 et 3. (On utilise toujours le QR code hôte dans "qrcodes/qrcode_host.png")

## Autre
- Il y a un bug avec la dernière fonction de la partie 3, les QR codes 0 et 3 sont bien extraits mais les autres ne le sont pas (problème avec une zone de Voronoï).
- Lien du GitHub : https://github.com/Realexx/PROJET_QR_CODE.git
