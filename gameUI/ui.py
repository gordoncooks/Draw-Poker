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

def displayHand(hand : list):

    result_string = ", ".join(hand)

    print("Your Hand: " + result_string + "" \
          "\n\n" \
          "1. Keep Hand" \
          "\n" \
          "2. Change Hand" \
          "\n")

def userInputPromt():
    userInput = input("Please select an option: ")
    return userInput