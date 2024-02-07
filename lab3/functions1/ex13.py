#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
print("Hello! What is your name?")
name=input()
print("\nWell, "+ name +", I am thinking of a number between 1 and 20.\nTake a guess.")

import random
def playing_game(number, x):
    x+=1
    a=int(input())
    if a==number:
        print("Good job, "+ name +"! You guessed my number in ", x," guesses!")
    elif a>number:
        print("\nYour guess is too high. \nTake a guess.")
        return playing_game(number, x)
    elif a<number:
        print("\nYour guess is too low. \nTake a guess.")
        return playing_game(number, x)

number=random.randint(1,20)
x=0
playing_game(number, x)