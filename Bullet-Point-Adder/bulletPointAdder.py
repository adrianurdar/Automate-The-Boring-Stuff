#! python3
# bulletPointsAdder.py - Adding bullets before each new line on the clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add bullets
lines = text.split('\n')

# Loop through all the lines in text
for i in range(len(lines)):
     # Add bullets to each of the line
     lines[i] = '* ' + lines[i]

# Make a single str line
text = '\n'.join(lines)

pyperclip.copy(text)
