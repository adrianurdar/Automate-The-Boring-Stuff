import random

numberOfStreaks = 0

for experimentNumber in range(10000):
     # Code that creates a list of 100 tails or heads
     list = []
     for i in range(100):
          if random.randint(0,1) == 0:
               list.append('H')
          else:
               list.append('T')

     # Code that checks if there is a streak of 6 heads or tails in a row
     s = 1
     for j in range(1, len(list)):
          if list[j] == list[j - 1]:
               s += 1
               if s == 6:
                    numberOfStreaks += 1
                    s = 1
          else:
               s = 1

print('Chance of streak if you flip the coin ' + str(experimentNumber + 1) + ' times: %s%%' % (numberOfStreaks / 100))
