from time import sleep
import random

from cards import generate_deck
from gameUI import ui

def main():
    
    while(True):
        ui.clear_terminal()             # Always clear terminal incase for mess
        ui.displayMainMenu()            # Display main menu
        userInput = ui.userInputPromt() # Ask for user value
        # Respond to user input
        match userInput:
            # Starts the game if 1 was selected
            case "1":
                ui.clear_terminal()             # Clear terminal once game start
                deck = generate_deck.makeDeck() # Create a fresh new card deck.
                random.shuffle(deck)            # This shuffles the curent list and does not return a list

            # Quit game if 2 was selected
            case "2":
                ui.clear_terminal()             # Clear terminal for goodbuy message
                print("Draw Poker says buy!")   # Display message
                sleep(1.5)                      # Gives user chance to read message
                ui.clear_terminal()             # Clear terminal for cleaning window
                break                           # Stops the main loop witch stops the game
            # If no case matched
            case _:
                ui.clear_terminal()     # Clear terminal for message
                print("Invalid option") # Display message
                sleep(1)                # Give user time to read message


if __name__ == "__main__":
    main()