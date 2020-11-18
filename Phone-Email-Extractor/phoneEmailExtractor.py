#! python3
# phoneEmailExtractor.py - Finding every phone number and email address in a long text on the clipboard

import pyperclip, re

def main():
     # Get the text off the clipboard.
     text = str(pyperclip.paste())

     # Create two regexes, one for matching phone numbers and the other for matching email addresses.
     # Phone regex
     phoneRegex = re.compile(r'''(
          (\d{3}|\(\d{3}\))?                 # Area code
          (\s|-|\.)?                         # Separator
          (\d{3})                            # First 3 digits
          (\s|-|\.)                          # Separator
          (\d{4})                            # Last 4 digits
          (\s*(ext|x|ext.)\s*(\d{2,5}))?     # Extension
          )''', re.VERBOSE)

     # Email regex
     emailRegex = re.compile(r'''(
          [a-zA-Z0-9_.%+-]+   # Username
          @                   # @ symbol
          [a-zA-Z0-9-.]+      # Domain name
          (\.[a-zA-Z]{2,4})   # .-something
          )''', re.VERBOSE)

     # Find all phone numbers and email addresses in the text.
     matches = []
     for groups in phoneRegex.findall(text):
          phoneNum = '-'.join([groups[1], groups[3], groups[5]])
          if groups[8] != "":
               phoneNum += ' x' + groups[8]
          matches.append(phoneNum)

     for groups in emailRegex.findall(text):
          matches.append(groups[0])

     # Copy the result to the clipboard
     if len(matches) > 0:
          pyperclip.copy('\n'.join(matches))
          print('Copied to clipboard: ')
          print('\n'.join(matches))
     else:
          # Display some kind of message if no matches were found in the text.
          print('No matches have been found.')

if __name__ == "__main__":
     main()
