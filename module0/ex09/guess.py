from random import randint

from numpy import number


def guess():
    '''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
'''
    attempts = 0
    number = randint(1, 99)
    while (True):
        n = input("What's your guess between 1 and 99?\n>> ")
        while (n.isdigit() is False):
            if (n == 'exit'):
                exit(print('Goodbye!'))
            print("That's not a number.")
            n = input("What's your guess between 1 and 99?\n>> ")
        n = int(n)
        attempts += 1
        if (n != number):
            print("too high" if n > number else "too low")
        else:
            exit(print("Congratulations, you've got it!\n\
You won in {} attempts!".format(attempts)))


print(guess.__doc__)
guess()
