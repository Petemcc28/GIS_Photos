import sys
import os
import PIL
import pyexiv2
from PIL import Image

topfolder = ""
subfolder = ""
src = ""
dest = ""
old_img = ""
new_img = ""


print("This script resizes the HQ photos")

def getfoldertype(topfolder):
    valid = ["Aerial", "Ground"]
    user_input_type = str(raw_input("Are the photos Aerial or Ground?: "))
    if user_input_type in valid:
        topfolder = "T:\Planning\\02_KPI_GIS\\09_Photos\\" + user_input_type
        return topfolder
    else:
        print("Folder must be Aerial or Ground... please check spelling.")
        return getfoldertype()
        
def getfoldername(subfolder):
    user_input_SUB = str(raw_input("Enter the new folder name: "))
    if len(user_input_SUB) == 8:
        subfolder = user_input_SUB
        return subfolder
    else:
        print("Folder name must be in format yyyymmdd... please try again.")
        return getfoldername()

topfolder = getfoldertype(topfolder)
subfolder = getfoldername(subfolder)
src = topfolder + "\\" + subfolder + "\\HQ"
dest = topfolder + "\\" + subfolder + "\\LQ"

def resize_img(old_img, new_img):
    basewidth = 300
    img = Image.open(old_img)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(new_img, guality = 50)

def copy_exif(old_img, new_img):
    m1 = pyexiv2.ImageMetadata(old_img)
    m1.read()
    m1.modified = True
    m2 = pyexiv2.metadata.ImageMetadata(new_img)
    m2.read()
    m1.copy(m2)
    m2.write()

for filename in os.listdir(src):
    if filename.endswith(".jpg"):
        old_img = src + "\\" + filename
        new_img = dest + "\\" + filename
        resize_img(old_img, new_img)
        copy_exif(old_img, new_img)
        print (old_img + " copied to " + new_img)
        continue
    else:
        continue

print("All photos resized")

