# This will generate and make the deck.
cardsRank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cardsSuit = ["H", "D", "C", "S"]

def makeDeck():
    """This makes a new card deck. The card deck is in order and not shuffled."""
    deck = []
    for cardSuit in cardsSuit:
        for cardRank in cardsRank:
            card = cardRank + cardSuit
            deck.append(card)
    return deck