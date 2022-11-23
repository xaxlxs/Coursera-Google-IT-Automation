from PIL import Image
import os
import sys

source = os.path.join(sys.path[0], "IMG_1020s.png")
output = "opt/icons/"

im = Image.open(source)
im.save("new_file.jpg")