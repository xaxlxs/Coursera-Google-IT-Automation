#!/usr/bin/env python3
import os
from PIL import Image
import glob

os.mkdir("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Scale-and-Convert/opt/")
os.mkdir("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Scale-and-Convert/opt/icons/")

for file in glob.glob('ic_*'):
	im = Image.open(file).convert('RGB')
	im.rotate(270).resize((128,128)).save("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Scale-and-Convert/opt/icons/" + str(file) + ".jpg")

"""
Psudo:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image in /opt/icons/ as .jpeg format
"""