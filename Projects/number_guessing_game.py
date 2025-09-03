# number_guessing_game.py
# Number Guessing Game

import random

print("🎯 Number Guessing Game 🎯")
number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("🎉 Correct! You guessed the number.")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
