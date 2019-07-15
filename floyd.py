# This is a guess game
import random

def floyd():

    print('\nAweome!  Let\'s play! I am thinking of a number between 1 and 20')
    secretNumber = random.randint(1, 20)

    for guessesTaken in range(1, 7):
        print('\nTake a guess')
        guess = int(input())

        if guess < secretNumber:
            print('\nYour guess is too low')
        elif guess > secretNumber:
            print('\nYour guess is too high')
        else:
            break # Condition for correct guess

    if guess == secretNumber:
        print('\nGood job,  person, You guessed my number in ' + str(guessesTaken ) + ' guesses')
    else:
        print('\nSorry.  My number was ' + str(secretNumber))

    input()
