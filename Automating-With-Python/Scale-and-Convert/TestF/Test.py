#!/usr/bin/env python3

import os, sys
from PIL import Image

# print(os.getcwd())

# im = Image.open("ic_map_black_48dp")
# im.save("new", "JPEG")


size = (128, 128)

for file in os.listdir():
    output = os.path.splitext(file)[0]
    try:
        with Image.open(file).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save("opt/icons/" + output, "JPEG")
    except OSError:
        pass

# import os, glob
# from PIL import Image

# newsize = 128, 128

# for file in glob.glob("ic_*"):
#     im = Image.open(file).convert('RGB')
#     im.rotate(270).resize((newsize)).save(file, "JPEG")