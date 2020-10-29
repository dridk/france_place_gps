## FRENCH_PLACE_COORD.tsv

Ce fichier contient l'ensemble des emplacements (capital, ville, village et hameau) extrait depuis [OpenStreeMap](https://download.geofabrik.de/europe/france.html) associés à leurs départements. 

- **name**: Le nom de l'emplacement 
- **place**: Le type d'emplacement (town,city,village,hamlet)
- **dep**: Le code du département 
- **latitude**: Latitude 
- **longitude**: Longitude

## Comment ont été générés ces fichiers ?
L'extraction des données à été réalisé avec l'outil [osmium](https://osmcode.org/osmium-tool/) sur les fichiers pbf de [geofabrik](https://download.geofabrik.de/europe/france.html).
Une découpe préalable de la carte par département a été réalisé à partir du fichier [departements-avec-outre-mer.geojson](https://github.com/gregoiredavid/france-geojson/blob/master/departements-avec-outre-mer.geojson)

## Usage 
### Prérequis 
Python3 et pandas :

    pip install pandas 

Osmium est disponible via le gestionnaire de package d'ubuntu:

    sudo apt install osmium-tools

### Lancement du script 

    ./script.sh 


## Source 

- https://osmcode.org/osmium-tool/
- https://download.geofabrik.de/europe/france.html
- https://github.com/gregoiredavid/france-geojson
