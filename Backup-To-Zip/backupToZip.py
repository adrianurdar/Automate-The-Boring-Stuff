# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, zipfile
from pathlib import Path
import time

"""
Backup the entire "folder" to zip 
"""
def backupZip(folder):
     # Make sure folder is absolute
     folder = os.path.abspath(folder)

     # Figure out what filename this folder should use based on what folder name exists
     number = 1
     while True:
          zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
          if not os.path.exists(zipFilename):
               break
          number += 1

     # Create the zip file
     print(f"Creating {zipFilename}...")
     # backupZipFile = zipfile.ZipFile(zipFilename, "w")
     time.sleep(1)

     # Walk through the folder tree and compress the files in each folder
     for foldername, subfolders, files in os.walk(folder):
          # Add the current folder to the zip
          print(f"Adding files in {foldername}...")
          # backupZipFile.write(foldername)
          time.sleep(1)

          # Add the files in zip
          for file in files:
               newBase = os.path.basename(folder) + "_"
               if file.startswith(newBase) and file.endswith(".zip"):
                    # Don't backup the backup zip files
                    continue
               # backupZipFile.write(os.path.join(foldername, file))
          # backupZipFile.close()

     print("Done.")

if __name__ == "__main__":
    backupZip(Path.cwd())
