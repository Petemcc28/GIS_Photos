import csv
import os

print ("This script renames the photos.")
newnames = str(raw_input("Enter the file to pull the new names from: "))

if len(newnames) == 8:
    with open(newnames + ".csv") as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
             oldPath = row[0]
             newPath = row[1]
             os.rename(oldPath, newPath)
else:
    print("File name expected in format yyyymmdd... please check and try again.")
    sys.exit(0)

