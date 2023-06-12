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