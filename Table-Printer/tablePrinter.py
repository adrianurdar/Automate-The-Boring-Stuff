# Write a function named printTable() that takes a list of lists of strings and 
# displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings.

tableData = [['apples', 'cherries', 'bananas', 'oranges', 'strawberry'],
     ['Al', 'Bob', 'Caro', 'David', 'Adrian'],
     ['dogs', 'cats', 'moose', 'goose', 'mice']]

def printTable(tableData):
     # Find the longest string in each of the inner lists
     colWidths = []
     for list in tableData:
          length = 0
          for words in list:
               value = len(words)
               if length < value:
                    length = value
          colWidths.append(length)

     # Print the data rjust(colWidths[i], ' ')
     for list in tableData:
          innerLength = len(list)
     
     for x in range(innerLength):
          for y in range(len(tableData)):
               print(tableData[y][x].rjust(colWidths[y], ' '), end=' ')
          print()

printTable(tableData)
