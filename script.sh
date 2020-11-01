#!/bin/sh

wget https://download.geofabrik.de/europe/france-latest.osm.pbf
wget https://download.geofabrik.de/europe/france/guadeloupe-latest.osm.pbf
wget https://download.geofabrik.de/europe/france/guyane-latest.osm.pbf
wget https://download.geofabrik.de/europe/france/martinique-latest.osm.pbf
wget https://download.geofabrik.de/europe/france/mayotte-latest.osm.pbf
wget https://download.geofabrik.de/europe/france/reunion-latest.osm.pbf

# # Merge all 
osmium cat *.pbf -o all.pbf -t node 

# # Keep only city, town, village and hamlet
osmium tags-filter all.pbf n/place=city,town,village,hamlet -o place.pbf --overwrite
osmium sort place.pbf -o place.order.pbf 


# Download geojson departement + outre mer 
wget https://github.com/gregoiredavid/france-geojson/raw/master/departements-avec-outre-mer.geojson
split geojson into departements 

python split_geojson.py

# Loop over each departement and extract a sub pbf file for each departements 
for dep in departements/*.geojson
do 
	output_1=${dep%%.geojson}.pbf
	output_2=${dep%%.geojson}.final.geojson

	osmium extract -p ${dep} place.order.pbf -o ${output_1} --overwrite
	osmium export -f geojson ${output_1} > ${output_2} --overwrite
done

# Merge all final.geojson into a tsv file 
python merge_geojson.py
