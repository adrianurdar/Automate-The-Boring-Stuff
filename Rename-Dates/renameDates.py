# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with US date format
datePattern = re.compile(r"""^(.*?)     # All text before the date
     ((0|1)?\d)-                        # One or two digits for the month
     ((0|1|2|3)?\d)-                    # One or two digits for the day
     ((19|20)\d\d)                      # Four digits for the year
     (.*?)$                             # All the text after the date
     """, re.VERBOSE)

# Go over the files in the working directory
for usFilename in os.listdir("."):
     mo = datePattern.search(usFilename)

     # Skip files without a date.
     if mo == None:
          continue

     # Get the different parts of the filename.
     beforePart = mo.group(1)
     monthPart = mo.group(2)
     dayPart = mo.group(4)
     yearPart = mo.group(6)
     afterPart = mo.group(8)

     # Form the European-style filename.
     euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

     # Get the full, absolute file paths.
     absWorkingDir = os.path.abspath(".")
     usFilename = os.path.join(absWorkingDir, usFilename)
     euroFilename = os.path.join(absWorkingDir, euroFilename)

     # Rename the files.
     print(f"Renaming {usFilename} to {euroFilename}...")
     # shutil.move(usFilename, euroFilename)
