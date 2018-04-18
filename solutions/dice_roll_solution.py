#!/usr/bin/python
# encoding=utf8


#The Goal
# Like the title suggets, this project involves writing a program that simulates rolling dice.
# When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other
# integer you prefer, the number of sides on the die is up to you.) The program will print what
# that number is. It should then ask you if you would like to roll again. For this project, you
# will need to set the min and max number that your die can produce. For the average die, that
# means a minimum of 1 and a maximum of 6. You will also want a fuction that randomly grabs a
# number within that range and prints it.

#Concepts to keep in mind:
# Random
# Integer
# Print
# While Loops

import random

#beginner
def roll():
    sides = 6
    number_rolled = random.randint(1, sides)
    print(number_rolled)

def main():
    input('Press enter to roll!')


#advanced
# def roll(sides):
#     number_rolled = random.randint(1, sides)
#     return number_rolled
# def main():
#     sides = 6
#     rolling = True
#     while rolling:
#         roll_again = input('Ready to roll? ENTER=Roll. Q=Quit.')
#         if roll_again.lower() != 'q':
#             number_rolled = roll(sides)
#             print('You rolled a', number_rolled)
#         else:
#             rolling = False
#     print('Thanks for playing!')

main()
roll()