from PIL import Image
import os
import sys

# source = os.path.join(sys.path[0], "IMG_1020s.png")
source = "/TestF/"
output = "/opt/icons/"

for file in source:
    im = Image.open(file)
    im.save(output + file, "JPEG")