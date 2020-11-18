"""
An application that takes a sandwich order

Sandwich Maker
Sandwich Menu:
Bread + protein = $10
Cheese = + $0.5
Mayo = + $0.5
Mustard = + $0.5
Lettuce = + $0.5
Lettuce = + $0.5
Tomato = + $1
"""

import pyinputplus as pyip

print('Welcome to the Fresh Food Factory!\n')
print("Let's configure your own sandwich.\n")
pyip.inputYesNo("Are you ready? ")

# Ask user for bread type
breadType = pyip.inputMenu(["wheat bread", "white bread", "sourdough bread"], numbered = True)

# Ask user for protein type
proteinType = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered = True)

# Initiate price for sandwich
price = 10.00

print("Right now your sandwich is " + breadType + " + " + proteinType)

# Ask user if he wants cheese
cheese = pyip.inputYesNo("Do you want cheese on your sandwich? ")
if cheese == "yes":
     cheeseType = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered = True)
     price += 0.5

# Ask user for toppings (mayo, mustard, lettuce, tomato)
topping = pyip.inputYesNo("Do you want mayo, mustard, lettuce or tomato on your sandwich? ")
if topping == "yes":
     topping1 = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered = True)
     if topping1 == "tomato":
          price += 1
     else:
          price += 0.5

# Ask user for number of sandwiches
numberOfSandwiches = pyip.inputInt("How many sandwiches do you want? ", min = 1)
price = price * numberOfSandwiches

# Show user the final order
if cheese == "yes":
     if topping == "yes":
          print("Your order: " + str(numberOfSandwiches) + " sandwiches (" + breadType + ", " + proteinType + ", " + cheeseType + ", " + topping1 + ")")
          print("Price: $" + str(price))
     else:
          print("Your order: " + str(numberOfSandwiches) + " sandwiches (" + breadType + ", " + proteinType + ", " + cheeseType + ", " + ")")
          print("Price: $" + str(price))
else:
     print("Your order: " + str(numberOfSandwiches) + " sandwiches (" + breadType + ", " + proteinType + ")")
     print("Price: $" + str(price))
