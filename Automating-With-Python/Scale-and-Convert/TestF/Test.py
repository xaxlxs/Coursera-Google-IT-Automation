#!/usr/bin/env python3

import os
import glob
from PIL import Image

for x in glob.glob("IM*"):
	new_image = Image.open(x).convert("RGB")
	new_image.rotate(270).resize((128,128)).save("/opt/icons/" + x,"JPEG")

# import os
# from PIL import Image

# os.getcwd()

# im = Image.open("IMG_1020s.png")
# im.save("new.png")