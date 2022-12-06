#!/usr/bin/env python3
import os, sys
from PIL import Image

size = (128, 128)

for file in os.listdir("/TestF/"):
    output = os.path.splitext(file)[0]
    try:
        with Image.open(file).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save("/opt/icons/" + output, "JPEG")
    except OSError:
        pass

# import os
# from PIL import Image

# os.getcwd()

# im = Image.open("IMG_1020s.png")
# im.save("new.png")