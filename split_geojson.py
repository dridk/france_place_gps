import json
import os

try:
    os.mkdir("departements")
except:
    pass

with open("departements-avec-outre-mer.geojson") as file:

    data = json.load(file)

    for item in data["features"]:
        p = item["properties"]
        code = p["code"]
        name = p["nom"]
        filename = f"departements/{code}.geojson"
        with open(filename, "w") as depfile:
            json.dump(item, depfile)
