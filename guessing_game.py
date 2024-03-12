import random

number = random.randint(1, 50)

while True:
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations, you guessed the number!")
        break

