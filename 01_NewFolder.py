import sys
import os

topfolder = ""
subfolder = ""

print("This script creates a new folder for photographs.")

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
newpath = topfolder + "\\" + subfolder
print ("New folders will be created at " + newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)
    os.makedirs(newpath + "\\LQ")
    os.makedirs(newpath + "\\HQ")
else:
    print ("Folder already exists. Please check and try again")
    sys.exit(0)

print("New folder created")
print("Please run resize script now")
