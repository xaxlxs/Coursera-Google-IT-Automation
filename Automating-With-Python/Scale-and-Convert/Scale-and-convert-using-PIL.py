from PIL import Image
source = "images/"
output = "opt/icons/"

im = Image.open("IMG_1020s.png")
im.save("new_file.jpg")