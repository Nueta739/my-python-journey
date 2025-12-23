#Modules------

import random
import math

#Welcome

print("Welcome to my Guessing Game!")
print("I am thinking of a number, try and guess it!\n")

#Variables ------------------------------------------------------

range = random.randint(1,10000)
secret_number = random.randint(1, range)
score = round(math.log2(range)) + 3
guess = int(input(f"Enter a number between 1 and {range}: "))
total_guesses = - round(math.log2(range)) - 3
#Main------------------------------------------------------
while True:
    if guess == secret_number:
        print(f"Congratulations!\nYou guessed the secret number correctly!")
        print(f"Your score is {score}!")
        break

    elif guess > range or guess < 1:
        guess = int(input(f"Invalid guess.\nEnter a number between 1 and {range}: "))
        score = score - 1
        if score < total_guesses:
            print(f"You are out of guesses. You lose!")
            break

    elif guess > secret_number:
        print("Lower!")
        guess = int(input(f"Enter a number between 1 and {range}: "))
        score = score - 1
        if score < total_guesses:
            print(f"You are out of guesses. You lose!")
            break

    else:
        print("Higher!")
        guess = int(input(f"Enter a number between 1 and {range}: "))
        score = score - 1
        if score < total_guesses:
            print(f"You are out of guesses. You lose!")
            break
