import random

guess=random.randint(1,50)


while(True):
    UserGuess=int(input("Guess A Number between 1 to 50"))

    if UserGuess > guess:
        print("Your guess is Too high!")
    if UserGuess < guess:
        print("Your guess is Too low!")
    if UserGuess == guess:
        print("Congrats, You Guessed the Number")
        break
