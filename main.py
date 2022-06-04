
import random

choices = ["Error", "Rock", "Paper", "Scissor"]
list1 = [1, 2, 3]
computer_choice = random.choice(list1)
computer_score = 0
user_score = 0


for _ in range(3):
    print("Enter your choice :  ")
    print(" \t1.Rock           \n \t2.Paper          \n \t3.Scissors       ")
    user_choice = int(input("> "))
    if (choices[computer_choice] == choices[user_choice]):
        print("computer choice - ",choices[computer_choice],"\t","You choice - ",choices[user_choice],"\n")
        print("It was a tie\n")
    elif (computer_choice+1) % 3 == user_choice:
        user_score = 1+user_score
        print("computer choice - ",choices[computer_choice],"\t","You choice - ",choices[user_choice],"\n")
        print("You wins\n")
    else:
        computer_score = 1+computer_score
        print("computer choice - ",choices[computer_choice],"\t","You choice - ",choices[user_choice],"\n")
        print("You failed\n")
print("------------------------------")
if user_score>computer_score:
    print("You wins")
elif user_score<computer_score:
    print("You failed")
else:
    print("It is a tie")