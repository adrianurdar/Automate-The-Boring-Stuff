# Conway's Game of Life

import random, time, copy

WIDTH = 8
HEIGHT = 8

# Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
     # Create a new column
     column = []

     for y in range(HEIGHT):
          if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
               # Add a living cell
               column.append("#")

          else:
               # Add a dead cell
               column.append(".")

     # nextCells is a list of column lists
     nextCells.append(column)

# Main program loop
while True:
     # Separate each step with newlines
     print('\n\n\n\n\n')
     currentCells = copy.deepcopy(nextCells)

     # Print currentCells on the screen
     for y in range(HEIGHT):
          for x in range(WIDTH):
               # Print the # or space
               print(currentCells[x][y], end="")

          # Print a newline at the end of the row
          print()

     # Calculate the next step's cells based on current step's cells
     for x in range(WIDTH):
          for y in range(HEIGHT):
               # Get neighboring coordinates
               # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
               leftCoord = (x - 1) % WIDTH
               rightCoord = (x + 1) % WIDTH
               aboveCoord = (y - 1) % HEIGHT
               belowCoord = (y + 1) % HEIGHT

               # Count the number of living neighbors
               numNeighbors = 0
               if currentCells[leftCoord][aboveCoord] == '#':
                    # Top-left neighbor is alive
                    numNeighbors += 1
               if currentCells[x][aboveCoord] == '#':
                    # Above neighbor is alive
                    numNeighbors += 1
               if currentCells[rightCoord][aboveCoord] == '#':
                    # Top-right neighbor is alive
                    numNeighbors += 1
               if currentCells[leftCoord][y] == '#':
                    # Left neighbor is alive
                    numNeighbors += 1
               if currentCells[rightCoord][y] == '#':
                    # Right neighbor is alive
                    numNeighbors += 1
               if currentCells[leftCoord][belowCoord] == '#':
                    # Below-left neighbor is alive
                    numNeighbors += 1
               if currentCells[x][belowCoord] == '#':
                    # Below neighbor is alive
                    numNeighbors += 1
               if currentCells[rightCoord][belowCoord] == '#':
                    # Below-right neighbor is alive
                    numNeighbors += 1

               # Set cell based on Conway's Game of Life rules
               if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive
                    nextCells[x][y] = '#'
               elif currentCells[x][y] == "." and numNeighbors == 3:
                    # Dead cells with 3 neghbors become alive
                    nextCells[x][y] = '#'
               else:
                    # Everything else dies or stays dead
                    nextCells[x][y] = "."

     # Add a 2 second pause to reduce flickering
     time.sleep(2)
