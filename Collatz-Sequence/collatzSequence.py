# Ask the user to input an integer
print("Enter number: ", end="")
number = input()


def collatz(number):
     if number % 2 == 0:
          return number // 2
     else:
          return 3 * number + 1

while True:
     try:
          # Run the Collatz Sequence
          number = int(number)
          print(collatz(number))
          if collatz(number) == 1:
               break
          number = collatz(number)

     # Catches if the user didn't input an integer
     except ValueError:
          print("Enter an integer: ", end="")
          number = input()
