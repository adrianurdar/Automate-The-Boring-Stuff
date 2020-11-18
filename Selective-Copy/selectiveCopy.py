# A program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
# Copy these files from whatever location they are in to a new folder.

from pathlib import Path
import pyinputplus as pyip
import os
import time
import shutil

def selectiveCopy(folder):
     # Make sure the path is absolute path
     folder = os.path.abspath(folder)

     # Choose what files will be copied (txt, jpg)
     print("Choose which files to be copied. ", end = "")
     fileExtension = pyip.inputChoice([".txt", ".jpeg", ".pdf", ".jpg"])

     # Figure out what filename this folder should use based on what folder name exists
     number = 1
     while True:
          newFolder = os.path.basename(folder) + "_copy_" + str(number)
          if not os.path.exists(newFolder):
               break
          number += 1

     # Create the new folder name
     print(f"Creating {newFolder}...")
     os.mkdir(newFolder)
     time.sleep(1)

     # Walk through the folder tree and copy the files in a new directory
     for foldername, subfolders, files in os.walk(folder):
          if newFolder in subfolders:
               subfolders.remove(newFolder)
          print(f"We're in {foldername}...")
          time.sleep(1)

          for file in files:
               if file.endswith(fileExtension):
                    print(f"Copying {file} in {newFolder}...")
                    shutil.copy(os.path.join(foldername, file), newFolder)
                    time.sleep(1)

     print("Done.")

if __name__ == "__main__":
    selectiveCopy(Path.cwd())
