import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playerchoice = input(
    "Enter 1 for ROCK\n      2 for PAPER\n      3 for SCISSORS\n")

computerchoice = random.choice(123)

player = int(playerchoice)

computer = computerchoice

print('You Choose ' + str(RPS(player)).replace('RPS.', ''))
print('Python Choose ' + str(RPS(computer)).replace('RPS.', ''))
print('')

if player == 1 and computer == 3:
    print('🎉 You win')
elif player == 2 and computer == 1:
    print('🎉 You win')
elif player == 3 and computer == 2:
    print('🎉 You win')
elif player == computer:
    print('😲 Tie game')
else:
    print('🐍 Python wins')
