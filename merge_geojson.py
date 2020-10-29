import json
import pandas as pd
from glob import glob
import re

items = []
for filename in glob("departements/*.final.geojson"):

    with open(filename) as file:

        data = json.load(file)

        dep_code = re.sub(r"departements/([\d|A|B]+)\.final\.geojson", r"\1", filename)

        for feature in data["features"]:

            prop = feature["properties"]
            lon, lat = feature["geometry"]["coordinates"]
            if "name" in prop:
                item = {
                    "name": prop["name"],
                    "place": prop["place"],
                    "dep": dep_code,
                    "latitude": lat,
                    "longitude": lon,
                }
                items.append(item)

pd.DataFrame(items).to_csv("FRENCH_PLACE_COORD.tsv", sep="\t", index=None)
