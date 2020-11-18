# A program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. 
# The results should be printed to the screen.

import pyinputplus as pyip
from pathlib import Path
import os
from posix import read
import re

def regexSearch():
     # Ask user for his expression
     expression = pyip.inputRegexStr("You want to search for: ")

     # Set counter for number of occurances
     expressionCounter = 0

     # Store all .txt files in a list
     directory = Path.cwd()
     allFiles = (list(directory.glob("*.txt")))
     for file in allFiles:
          # Open all .txt files in the folder
          currentFile = open(file, "r")
          content = currentFile.read()
          currentFile.close()

          # Search user expression in the file
          for match in re.finditer(expression, content):
               expressionCounter += 1

     print("The expression occured " + str(expressionCounter) + " times")


if __name__ == "__main__":
    regexSearch()
