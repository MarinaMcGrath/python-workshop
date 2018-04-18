#!/usr/bin/python
# encoding=utf8

# The Goal:
# Create a program that will simulate a blackjack game.
# 1. Define your functions:
    # - hit() or deal_card()
    # - dealerDraw(dealerScore)
    # - checkWin(dealerScore,playerScore)
    # - isBust(score)
# 2. Make a variable called endGame and set it equal to False
# 3. Make a loop that only runs while endGame is False (i.e. the game has not ended)
# 4. Inside the loop, get input from the player to ask what he wants to do
    # a. If his input was “stick”
        # i. print out his total and the dealer’s total
        # ii. check who has won and print it
        # iii. end the game
    # b. If his input was “hit”:
        # i. draw him a new card and add it to his total
        # ii. check if he has bust – if so the game ends and he loses, if not print his
        # new total
        # iii. if he didn’t bust, decide whether the dealer will draw
        # iv. check if the dealer is bust – if so the game ends and the player wins

def main():
    print('Hello World')


main()