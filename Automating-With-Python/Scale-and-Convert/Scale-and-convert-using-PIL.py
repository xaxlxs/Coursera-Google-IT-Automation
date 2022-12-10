#!/usr/bin/env python3

##########################################
# Run this script from the images folder #
##########################################


import os
from PIL import Image
import glob

# os.mkdir("/opt/")
# os.mkdir("/opt/icons/")

for file in glob.glob('ic_*'):
	im = Image.open(file).convert('RGB')
	name, ext = os.path.splitext(file)
	output = "/opt/icons/" + file
	im.rotate(270).resize((128,128)).save(output, "JPEG")

"""
Psudo:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image in /opt/icons/ as .jpeg format
"""