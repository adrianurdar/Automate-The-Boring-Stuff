# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
# with "and" inserted before the last item.

import sys

# Define the initial list
spam = []

# Ask the user for list items
list = input("Enter your list: ")

# Check if list is empty
if not list:
     print("Empty list.")
     sys.exit()

# Split the elements into a list
list = list.split()

def andFunction(spam):
     # Catch if the user list has only 1 element
     if len(spam) == 1:
          return "{}".format(spam[0])

     # Catch if the user list has 2 or more elements
     else:
          for i in spam[:-1]:
               return "{} and {}".format(", ".join(spam[:-1]), spam[-1])


# Print the result
print("User list is:", andFunction(list))
