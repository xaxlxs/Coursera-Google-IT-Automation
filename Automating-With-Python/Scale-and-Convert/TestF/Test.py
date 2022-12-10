#!/usr/bin/env python3

# import os
# from PIL import Image

# im = Image.open("ic_map_black_48dp").convert('RGB')
# im.save("new.jpeg", "JPEG")


# size = (128, 128)

# for file in os.listdir():
#     output = os.path.splitext(file)[0]
#     try:
#         im = Image.open(file)
#         im.convert('RGB')
#         im.save(output, "JPEG")
#     except OSError:
#         pass

# import os, glob
# from PIL import Image

# newsize = 128, 128

# for file in glob.glob("ic_*"):
#     im = Image.open(file).convert('RGB')
#     im.rotate(270).resize((newsize)).save(file, "JPEG")

#!/usr/bin/env python3
import os
from PIL import Image
import glob

os.mkdir("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Scale-and-Convert/opt/")
os.mkdir("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Scale-and-Convert/opt/icons/")

for file in glob.glob('ic_*'):
	im = Image.open(file).convert('RGB')
	im.rotate(270).resize((128,128)).save("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Scale-and-Convert/opt/icons/" + str(file) + ".jpg")