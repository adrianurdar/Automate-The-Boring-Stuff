# An application that generates 10 random multiplication questions

import pyinputplus as pyip

import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
     # Pick 2 random numbers
     num1 = random.randint(0, 9)
     num2 = random.randint(0, 9)

     prompt = f"#{(questionNumber + 1)}: {num1} x {num2} = "
     try:
          # Right answer handled by allowRegex
          # Wrong answer handled by blockRegex
          pyip.inputStr(prompt, allowRegexes = [f"^{(num1 * num2)}$"], blockRegexes = [(".*", "Incorrect")], 
                         timeout = 8, limit = 3)
     
     # If user runs out of time
     except pyip.TimeoutException:
          print("Out of time!")

     # If user runs out of tries
     except pyip.RetryLimitException:
          print("Out of tries!")
     
     # If users answers correctly
     else:
          print("Correct!")
          correctAnswers += 1

     # Pause to let the user read the message
     time.sleep(1)

# Print the final score     
print(f"Score: {correctAnswers} / {numberOfQuestions}")
