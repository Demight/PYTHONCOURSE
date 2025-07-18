import random
computer_choice = random.choice(["scissors","rock","scissors"])
user_choice = input("Input your choice: rock or paper or scissors: ")
print("Computer Choice:", computer_choice)

if user_choice == computer_choice:
    print("Tie")
elif user_choice == 'rock' and computer_choice == "scissors":
    print("Win")
elif user_choice == 'paper' and computer_choice == "rock":
    print("Win")
elif user_choice == 'scissor' and computer_choice == "paper":
    print("Win")
else:
    print("Computer win")
print("Thanks for playing!")
