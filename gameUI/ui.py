import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayMainMenu():
    print("Welcome To Draw Poker!" \
    "\n\n" \
    "1. Start Game" \
    "\n" \
    "2. Quit Game" \
    "\n")

def userInputPromt():
    userInput = input("Please select an option: ")
    return userInput