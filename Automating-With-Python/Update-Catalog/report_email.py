#!/usr/bin/env python3

import os
import glob
from datetime import datetime
import reports

# Verify source location in Qwiklabs
source = "supplier-data/descriptions"

os.chdir(source)

paragraph = ""

for file in glob.glob("*.txt"):
    with open(file) as reader:
        # print(reader.readlines())
        name = reader.readline().strip()
        weight = reader.readline().strip()
        # print(name, weight)
        paragraph += "name: " + name + "\n" + "weight: " + weight + "\n\n"
print(paragraph)