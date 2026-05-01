print("Please Enter your Name")
a = input("Enter Name : ")
print("Welcome to the game " + a)

import random
from random import randint

def game(player_name):
    print("Guess the number between 1 and 10")
    number = random.randint(10,50)
    guess = 0
    attempts = 0  # Counter for the number of attempts

    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment attempts for each guess
        if guess < number:
            print("Too low! Try again❎")
        elif guess > number:
            print("Too high! Try again❎")

    print("Congratulations! You guessed the number! 🎉")

    # Record the score in a text file
    with open("scores.txt", "a") as file:
        file.write(f"Player: {player_name}, Attempts: {attempts}\n")

while True:
    print("Please Enter your Name")
    player_name = input("Enter Name : ")
    print("Welcome to the game " + player_name)

    game(player_name)

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing! Goodbye! 👋")
        break
