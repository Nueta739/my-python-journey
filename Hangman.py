#Hangman game
import random
easy_words = [
    "apple", "banana", "orange", "grape", "lemon", "melon", "berry", "peach", "mango", "plum",
    "cat", "dog", "mouse", "tiger", "zebra", "horse", "sheep", "goose", "shark", "eagle",
    "blue", "green", "yellow", "purple", "brown", "black", "white", "gray", "silver", "gold",
    "car", "train", "plane", "truck", "boat", "bike", "ship", "motor", "rocket", "wagon",
    "pizza", "bread", "cheese", "cookie", "donut", "taco", "salad", "butter", "candy", "honey",
    "rain", "storm", "cloud", "snow", "sunny", "wind", "sky", "river", "ocean", "island",
    "chair", "table", "couch", "plate", "spoon", "knife", "brush", "phone", "clock", "light",
    "happy", "laugh", "smile", "dance", "party", "magic", "brave", "strong", "funny", "giant"
]
medium_words = [
    "pumpkin", "avocado", "broccoli", "spinach", "lasagna", "pancake", "sausage", "chicken", "mustard", "cinnamon",
    "penguin", "flamingo", "elephant", "gorilla", "dolphin", "kangaroo", "reptile", "butterfly", "tarantula", "toucan",
    "rainbow", "sunlight", "thunder", "tornado", "volcano", "tsunami", "horizon", "eclipse", "planet", "gravity",
    "teacher", "student", "library", "college", "museum", "stadium", "airport", "harbor", "factory", "freezer",
    "blanket", "curtain", "cabinet", "compass", "pillow", "lantern", "battery", "mirror", "notebook", "package",
    "journey", "adventure", "fortune", "kingdom", "mystery", "treasure", "believe", "courage", "freedom", "victory"
]
hard_words = [
    "xylophone", "pneumonia", "chrysalis", " labyrinth", "encyclopedia", "microscope", "pharaoh", "espionage", "marathon", "parachute",
    "avalanche", "camouflage", "cathedral", "courtyard", "hieroglyph", "boulevard", "crescendo", "miraculous", "rhinoceros", "tsunami",
    "conqueror", "brilliant", "enigmatic", "hologram", "illuminate", "juxtapose", "kilometer", "metaphor", "paradox", "republic",
    "symphony", "tournament", "university", "vocabulary", "wilderness", "wristwatch", "zookeeper", "apocalypse", "hemisphere", "phenomenon"
]
difficulties = ['easy','medium','hard']
score = 0
result = ""

print("Welcome to Hangman!")

difficulty = str(input("Choose your difficulty! Enter easy medium or hard: ")).lower()
while difficulty  not in difficulties:
    difficulty = str(input("Invalid choice. Enter easy, medium or hard! "))
print(f"Difficulty selected: {difficulty}")

if difficulty == 'easy':
    word = random.choice(easy_words)
    score = 6
elif difficulty == 'medium':
    word = random.choice(medium_words)
    score = 8
else:
    word = random.choice(hard_words)
    score = 10

#need to add some sort of code which finds out the number of characters in the word, and then prints that many underscores to show how many characters

length = len(word)
shown = "_" * length
sub = list(shown)




#something like this; guess = a letter, checks if letter is in word, if it is, finds its index, replaces the _ in shown with that letter

while score >= 0:
    print("".join(sub))
    guess = input("Guess a letter: ")
    if len(guess) != 1:
        guess = str(input("Invalid guess. Please enter a single letter: "))

    if guess in word:
        print("Correct!")
        location = word.find(guess)
        sub[location] = guess
        if "".join(sub) == word:

            print("Congrats! You guessed the word!")
            result = "You Win!"
            #implement end/ retry menu
#when word has two letters code only reveals first location in word.


    else:
        print("Incorrect Guess! Try again!")
        score -= 1


if score <= 0:
    result = "You lose!"
    print(f"{result}")
    print("Thank you for playing!")