#!/usr/bin/env python3
import os
import glob
import requests

url = "http://localhost/upload/"

# Verify source directory when running in Qwiklabs
source = "supplier-data/images/"
os.chdir(source)

for file in glob.glob("*.jpeg"):
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
        