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
        name = reader.readline()
        weight = reader.readline()
        description = reader.readline()
        dict = {"name": name.strip(), "weight": weight.strip(" lbs\n"), "description": description.strip(), "image_name": image_file}
        data_json = json.dumps(dict)
        # print(data_json)
        response = requests.post(address, json=dict)
        # print(response.status_code)