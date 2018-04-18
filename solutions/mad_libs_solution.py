#!/usr/bin/python
# encoding=utf8

# The Goal:
# The program will first prompt the user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc.
# Then, once all the information has been inputted, the program will take that data and place them into a premade story template.
# You’ll need prompts for user input, and to then print out the full story at the end with the input included.

# Concepts to keep in mind:
# Strings
# Variables
# Concatenation
# Print

#solution 1
madlib = "There was once a "
hero = input("Let's see a noun: ")
madlib += (hero + " that set out for a ")
goal = input("Another noun, please: ")
madlib += (goal + ".  But on the way past a ")
place = input("How about a place: ")
madlib += place
villain = input("A person this time: ")
action = input("A past tense verb: ")
madlib += ", {} ran out of {} with the {} first.".format(villain, place, goal)

print(madlib)

#solution 2
adjective1 = input("Tell me an adjective, and click enter. ")
noun1 = input("Tell me a noun (plural), and click enter. ")
noun2 = input("Tell me another noun, and click enter. ")
adjective2 = input("Tell me an another adjective, and click enter. ")

print("Roses are " + adjective1)
print(noun1 + " are blue")
print(noun2 + " is " + adjective2)
print("And so are you!")