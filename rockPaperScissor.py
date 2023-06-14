<<<<<<< HEAD
import random
list =["rock","paper","scissor"]


i=3
while(i>0):
    text = random.choice(list)
    #print(text)
    User = input("Enter Your choice::::")
    if(text in list):
        if (text== "rock" and  User  == "scissor")or(text == "paper" and User == "rock")or(text == "scissor" and User == "paper"):
            print("Your Choice is",User,"computer's choice is",text)
            print("Computer Won")
        elif text==User:
            print("Your Choice is",User,"computer's choice is",text)
            print("It's a tie!")
        else:
            print("Your Choice is",User,"computer's choice is",text)
            print("You won!")
    else:
        print("Invalid choice")
    i-=1


#     #
# import random

# choices = ["rock", "paper", "scissors"]

# while True:
#     computer_choice = random.choice(choices)
#     user_choice = input("Choose rock, paper, or scissors: ")
#     if user_choice not in choices:
#         print("Invalid choice! Please choose again.")
#     else:
#         print("You chose %(user_choice)s, and the computer chose %(computer_choice)s."%locals())
#         if user_choice == "rock" and computer_choice == "scissors":
#             print("You win!")
#         elif user_choice == "paper" and computer_choice == "rock":
#             print("You win!")
#         elif user_choice == "scissors" and computer_choice == "paper":
#             print("You win!")
#         elif user_choice == computer_choice:
#             print("It's a tie!")
#         else:
#             print("Computer wins!")
=======
import random
list =["rock","paper","scissor"]


i=3
while(i>0):
    text = random.choice(list)
    #print(text)
    User = input("Enter Your choice::::")
    if(text in list):
        if (text== "rock" and  User  == "scissor")or(text == "paper" and User == "rock")or(text == "scissor" and User == "paper"):
            print("Your Choice is",User,"computer's choice is",text)
            print("Computer Won")
        elif text==User:
            print("Your Choice is",User,"computer's choice is",text)
            print("It's a tie!")
        else:
            print("Your Choice is",User,"computer's choice is",text)
            print("You won!")
    else:
        print("Invalid choice")
    i-=1
>>>>>>> 7324b90fcfd9e427bc3d071c2156a8aaed742496
