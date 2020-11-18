# Ask the user to guess a number in X guesses
import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. In how many tries you want to guess it?")
tries = int(input())

# Ask the player to guess
for guessesTaken in range(1, tries + 1):
     print("Take a guess.")
     guess = int(input())

     if guess < secretNumber:
          print("Your guess is too low.")
     elif guess > secretNumber:
          print("Your guess is too high.")
     else:
          break # The player guessed correctly

if guess == secretNumber:
     print("Good job! You guessed my number in " + str(guessesTaken) + " guesses.")
else:
     print("Nope. The number I was thinking was " + str(secretNumber))
