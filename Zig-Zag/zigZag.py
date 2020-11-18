import time, sys

# How many spaces to indent.
indent = 0

# Whether the indentation is increasing or not.
indentIncreasing = True

try:
     # The main program loop.
     while True:
          print(" " * indent, end="")
          print("********")

          # Pause for 1/10 of a second.
          time.sleep(0.1)

          if indentIncreasing:
               # Increase the number of spaces:
               indent = indent + 1
               if indent == 20:
                    # Change direction:
                    indentIncreasing = False

          else:
               # Decrease the number of spaces:
               indent = indent - 1
          
          if indent == 0:
               # Change direction:
               indentIncreasing = True

except KeyboardInterrupt:
     sys.exit()
