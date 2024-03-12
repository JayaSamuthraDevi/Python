import random

choices = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ")
    if user_choice not in choices:
        print("Invalid choice! Please choose again.")
    else:
        print("You chose %(user_choice)s, and the computer chose %(computer_choice)s."%locals())
        if user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        elif user_choice == computer_choice:
            print("It's a tie!")
        else:
            print("Computer wins!")

