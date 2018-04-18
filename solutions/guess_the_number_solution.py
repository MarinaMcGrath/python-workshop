#!/usr/bin/python
# encoding=utf8

# The Goal:
# Similar to the first project, this project also uses
# the random module in Python. The program will first
# randomly generate a number unknown to the user. The
# user needs to guess what that number is. (In other
# words, the user needs to be able to input information.)
# If the user’s guess is wrong, the program should
# return some sort of indication as to how wrong (e.g.
# The number is too high or too low). If the user
# guesses correctly, a positive indication should appear.
# You’ll need functions to check if the user input is an
# actual number, to see the difference between the inputted
# number and the randomly generated numbers, and to then
# compare the numbers.

# Concepts to keep in mind:
# Random function
# Variables
# Integers
# Input/Output
# Print
# While loops
# If/Else statements
import random

def is_valid_number(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

def main():
    number = random.randint(1, 100)
    guessed_number = False
    guess = input('Guess a number between 1 and 100: ')
    num_guesses = 0
    while not guessed_number:
        if not is_valid_number(guess):
            guess = input("I won't count that one. A number between 1 and 100, please: ")
            continue
        else:
            num_guesses += 1
            guess = int(guess)
        if guess < number:
            guess = input('Too low. Guess again: ')
        elif guess > number:
            guess = input('Too high. Guess again: ')
        else:
            print('You got it in', num_guesses, 'guesses!')
            guessed_number = True

    print('Thanks for playing')


main()