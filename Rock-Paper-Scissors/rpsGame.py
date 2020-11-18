import random, sys

print("Welcome to ROCK, PAPER, SCISSORS!")

# Keep track of the wins, losses and ties
wins = 0
losses = 0
ties = 0

# The main game loop
while True:
     print("%s Wins, %s Ties, %s Losses" %(wins, ties, losses))

     # The player input loop
     while True:
          print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit.")
          playerMove = input()

          if playerMove == "q":
               # Quit the game
               sys.exit()

          if playerMove == "r" or playerMove == "p" or playerMove == "s":
               # Accept the input and break the loop
               break

          print("Type one of r, p, s, or q.")

     # Display what the player chose
     if playerMove == "r":
          print("ROCK versus...")
     elif playerMove == "p":
          print("PAPER versus...")
     else:
          print("SCISSORS versus...")

     # Display what the computer chose
     randomNumber = random.randint(1,3)
     if randomNumber == 1:
          computerMove = "r"
          print("ROCK")
     elif randomNumber == 2:
          computerMove = "p"
          print("PAPER")
     else:
          computerMove = "s"
          print("SCISSORS")

     # Display and record the result
     if playerMove == computerMove:
          print("It's a tie!")
          ties += 1
     elif playerMove == "r" and computerMove == "p":
          print("You lose.")
          losses +=1
     elif playerMove == "r" and computerMove == "s":
          print("You win!")
          wins +=1
     elif playerMove == "p" and computerMove == "r":
          print("You win!")
          wins += 1
     elif playerMove == "p" and computerMove == "s":
          print("You lose.")
          losses += 1
     elif playerMove == "s" and computerMove == "r":
          print("You lose.")
          losses += 1
     else:
          print("You win!")
          wins += 1
