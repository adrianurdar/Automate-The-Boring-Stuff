# mcb.pyw - saves and loads pieces of text to clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
# Usage: py.exe mcb.pyw delete <keyword> - Deletes clipboard to keyword
# Usage: py.exe mcb.pyw <keyword> - Copies keyword to clipboard
# Usage: py.exe mcb.pyw list - Loads all keywords to clipboard

import pyperclip, shelve, sys

mcbShelf = shelve.open("mcb")
command = sys.argv[1].lower()
nonKeywords = ["list", "save", "delete"]
usage = f"# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword\n# Usage: py.exe mcb.pyw delete <keyword> - Deletes clipboard to keyword\n# Usage: py.exe mcb.pyw <keyword> - Copies keyword to clipboard\n# Usage: py.exe mcb.pyw list - Loads all keywords to clipboard"

if len(sys.argv) == 3:
     keyword = sys.argv[2].lower()
     if keyword in nonKeywords:
          print("Cannot use keyword as 'list', 'save' or 'delete'.")
     elif command == "save":
          mcbShelf[keyword] = pyperclip.paste()
          print("Text saved!")
     elif command == "delete":
          del mcbShelf[keyword]
          print("Text deleted!")
elif len(sys.argv) == 2:
     if command == "list":
          for key in list(mcbShelf.keys()):
               print(str(key))
     elif command in mcbShelf:
          pyperclip.copy(mcbShelf[command])
          print("Text copied!")
     else:
          print("Keyword not found. Type py.exe mcb.pyw list to load all keywords.")
else:
     print(f"Usage invalid\n" + usage)

mcbShelf.close()
