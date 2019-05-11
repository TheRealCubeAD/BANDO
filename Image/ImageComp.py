from PIL import Image
import os
import shutil

p_from = "input/"
p_to = "output/"

formats = ["jpg","jpeg","png","raw","dng"]

files = os.listdir(p_from)
print("Starting...")
print(files)
print()

for file in files:
    print(file)
    if file.split(".")[-1].lower() in formats:
        print("Image: TRUE")
        print("Opening...")
        image = Image.open(p_from+file)
        print("Prozessing...")
        image = image.resize((2250,1500),Image.ANTIALIAS)
        print("Saving...")
        image.save(p_to+file,quality=80)
    else:
        print("Image: FALSE")
    print()
