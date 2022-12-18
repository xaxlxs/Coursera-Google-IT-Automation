#!/usr/bin/env python3

import os
from PIL import Image
import glob

# Verify source directory when running in Qwiklabs
source = "supplier-data/images/"

os.chdir(source)

for file in glob.glob("*.tiff"):
    im = Image.open(file).convert('RGB')
    name, ext = os.path.splitext(file)
    im.resize((600,400)).save(name + ".jpeg")
