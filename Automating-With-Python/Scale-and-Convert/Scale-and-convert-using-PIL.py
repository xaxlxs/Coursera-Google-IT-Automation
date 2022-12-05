#!/usr/bin/env python3

import os
import glob
import sys
from PIL import Image

"""
Psudo:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image in /opt/icons/ as .jpeg format
"""

# source = os.path.join(sys.path[0], "IMG_1020s.png")
# image1 = Image.open(source + "ic_map_black_48dp")
# image1.save("newblack_48dp.jpg")

source = "/images/"
output = "/opt/icons/"
rotation = 270
size = 128, 128

for file in source:
    im = Image.open(file)
    im.rotate(rotation).resize((size)).save(output + file, "JPEG")
    
    # Hide the below lines to test
    # im = im.convert("RGB")    
    # Hide the above lines to test
