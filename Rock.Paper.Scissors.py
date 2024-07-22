import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        ZERO = 0

    playerchoice = (
        input("Enter...\n 1 for Rock \n 2 for Paper \n 3 for Scissors\n"))

    computerchoice = random.choice([1, 2, 3])

    player = int(playerchoice)

    computer = int(computerchoice)

    print('\nyou chose: ' + str(RPS(player)).replace('RPS.', '').title() + '.')
    print('python chose: ' + str(RPS(computer)).replace('RPS.', '').title() + '.')
    print('')

    if player == (123):
        print("ok...")
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

    elif player == (4567890):
        print('must enter 1, 2, or 3')
        return play_rps()

    else:
        print('')

    print('playagain?')

    while True:
        playagain = input(
            '\nY for yes\nQ to quit\n\n')

        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print('\n🎉🎉🎉😲')
        print("Thank you for playing")
        playagain = False
        sys.exit


play_rps()
