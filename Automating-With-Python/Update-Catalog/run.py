#! /usr/bin/env python3

import os
import glob
import json
import requests

# Verify address and source in Qwiklabs
address = "http://<corpweb-external-IP>/feedback"
source = "supplier-data/descriptions"

os.chdir(source)

for file in glob.glob("*.txt"):
    with open(file) as reader:
        name, ext = os.path.splitext(file)
        image_file = name + ".jpeg"
        # print(reader.readlines())
        name = reader.readline().strip()
        weight = reader.readline().strip(" lbs\n")
        weight = int(weight)
        description = reader.readline().strip()
        dict = {"name": name, "weight": weight, "description": description, "image_name": image_file}
        # data_json = json.dumps(dict)
        response = requests.post(address, json=dict)
        print(response.status_code)
