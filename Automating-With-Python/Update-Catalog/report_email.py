#!/usr/bin/env python3

import os
import glob
from datetime import datetime
import json
import reports

# Verify source location in Qwiklabs
source = "supplier-data/descriptions"

os.chdir(source)

for file in glob.glob("*.txt"):
    with open(file) as reader:
        name, ext = os.path.splitext(file)
        image_file = name + ".jpeg"
        # print(reader.readlines())
        name = reader.readline()
        weight = reader.readline()
        dict = {"name": name.strip(), "weight": int(weight.strip(" lbs\n"))}
        data_json = json.dumps(dict)
        print(data_json)