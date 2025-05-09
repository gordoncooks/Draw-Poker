from time import sleep
import random

from cards import generate_deck
from gameUI import ui

def main():
    
    while(True):
        cardDeckIndex = 0
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

                # Players:
                players = [[],[],[],[],[]]

                # Give cards to players
                while(True):
                    # Check last player total hands
                    player_hand_checker = players[4]
                    hand_len = len(player_hand_checker)
                    if hand_len == 5:
                        break
                    else:
                        # Give cards to players
                        for player in players:
                            player.append(deck[cardDeckIndex])
                            cardDeckIndex += 1

                # Assing hand to player and opponents
                playerHand = players[0]
                oponent1 = players[1]
                oponent2 = players[2]
                oponent3 = players[3]
                oponent4 = players[4]

                # Show player their hand hands
                ui.displayHand(playerHand)
                
                userInput = ui.userInputPromt()
                

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