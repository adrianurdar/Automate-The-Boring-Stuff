# madLibs.py - reads in text files and lets the user add their own text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

# Usage: madLibs.py

import re
from pathlib import Path
import sys

def madLib():
     # Ask user to name the file he wants to read
     fileName = input("Name the file you want to read: ")

     # Check if the filename exists
     try:
          # Open the file
          fileInput = open(fileName + ".txt")
     except FileNotFoundError:
          print(fileName + ".txt does not exist.")
          sys.exit()

     # Read the content of the file
     fileContent = fileInput.read()

     # Search for ADJECTIVE in the text and replace them
     fileContent = re.sub(r'ADJECTIVE', input('Enter an adjective:\n'), fileContent)

     # Search for NOUN in the text and replace them
     fileContent = re.sub(r'NOUN', input('Enter a noun:\n'), fileContent)

     # Search for VERB in the text and replace them
     fileContent = re.sub(r'VERB', input('Enter a verb:\n'), fileContent)

     # Search for ADVERB in the text and replace them
     fileContent = re.sub(r'ADVERB', input('Enter an adverb:\n'), fileContent)

     # Save the corrected text in a file
     fileName = input("Save file as: ")
     fileOutput = open(fileName + '.txt', 'w')
     fileOutput.write(fileContent)

     # Print that file to the terminal
     print(fileContent)


if __name__ == "__main__":
    madLib()
