import random

score = 0
print("---------------------------------")
print("")
print("Welcome to Rock, Paper, Scissors!")
print("")
print("---------------------------------\n")

while True:
    valid_choices = ["rock", "paper", "scissors"]
    user_choice = str(input("Enter rock, paper, or scissors: ")).lower()
    while user_choice not in valid_choices:
        user_choice = str(input("Invalid choice, Enter rock, paper, or scissors: ")).lower()


    print(f"You chose: {user_choice}")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    result = ""
    if user_choice == computer_choice:
        result = "Its a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
        score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
        score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
        score += 1
    else:
        result = "You lose!"
        score -=1

    print(result)
    repeat = str(input("Would you like to play again? Press y to keep playing press any other key to exit: ")).lower()
    if repeat == "y":
        continue
    else:
        print("Thank you for playing!")
        print(f"Your final score is: {score}")
        break
