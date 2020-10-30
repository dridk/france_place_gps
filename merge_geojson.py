import json
import pandas as pd
from glob import glob
import re


def name_from_geojson(filename):
    with open(filename) as file:

        data = json.load(file)

        return data["properties"]


items = []
for filename in glob("departements/*.final.geojson"):

    with open(filename) as file:

        data = json.load(file)

        base_name = filename.replace(".final", "")

        dep_info = name_from_geojson(base_name)

        dep_code = dep_info["code"]
        dep_name = dep_info["nom"]

        for feature in data["features"]:

            prop = feature["properties"]
            lon, lat = feature["geometry"]["coordinates"]
            if "name" in prop:

                postcode = prop.get("addr:postcode", f"")

                item = {
                    "name": prop["name"],
                    "place": prop["place"],
                    "postcode": postcode,
                    "depcode": dep_code,
                    "depname": dep_name,
                    "latitude": lat,
                    "longitude": lon,
                }
                items.append(item)

pd.DataFrame(items).to_csv("FRENCH_PLACE_COORD.tsv", sep="\t", index=None)
