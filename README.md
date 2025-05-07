# Draw Poker

Draw poker is a poker variant where players receive a full hand initially and then have the option to discard and draw new cards to improve their hand.

> I will updating this README file as I am working on this project. 
> * Start Date 07 May 2025.
> * End Date: N/A

## How the game works

### Starting the game

The player gets a main menu with the following options:
```txt
Welcom to Draw Poker!

1. Start
2. Quit

Select an option: 
```

To select an option, type the number that corelates to what you want to do and press enter. When selecting 1 the game will start. When selecting 2 the game will exite and the window will close.

### In the game

The player will see the 5 cards given to them in a list with each card also having a number. The the user kan then select to keep or to Change cards.

```txt
Your Hand: 10H, JH, QH, KH, AH 

1. Keep Cards
2. Change Cards

Select an option: 
```
If the user decided to keep the cards, the cards will be revield of the other openents and the game will check who has the best hand. If the user selected to change there card the game will show:

```txt
Cards To Change:

1. 10H
2. JH
3. QH
4. KH
5. AH 

List your cards: 
```

The user will need to list there cards as:

```txt
List your cards: 1, 4, 2, 5
```
> The player can select the maximum of 4 cards and if the pleyer do decide to still keep the crads they can just type "C" or "c" for cancle.

Once the new cards are ready the user will see there hand again and only one option will be avaulible and that will be contenue:

```txt
Your New Hand: KH, 7D, 2C, QS, 5C
```

### End of game
You will be in the ending once the your cards and your opponents cards a shown as follow with the winner anounec at the bottom of the listed cards with 2 options:

```txt
End of Game!

Your Hand: KH, 7D, 2C, QS, 5C | High Card | 
Opponent 1 Hand: 7S, 7C, 7H, AD, JD | Thee Of a Kind |
Opponent 2 Hand: 4S, 8H, 9H, 4C, AS | Double |
Opponent 3 Hand: 2S, 3H, 4H, 5S, 6S | Striaght |
Opponent 4 Hand: 
```

## How to read the cards

### Simbols
The game does not use card simbles (Will maby be added later). The letters of each card represents (aka suit):

* H = Harts
* D = Dimonds
* S = Spades
* C = Clovers

## How the scoreing works

The game will look and see what hand you have it will start and compare with the strongest hand till the lowest like below:

* Royal Flush: A-K-Q-J-10 All the same suit.
* Straight Flush: Five consecutive cards in the same suit.
* Four of a Kind: Four cards of the same rank.
* Full House: Three cards of the same  rank and two of another.
* Flush: Five cards of the same suit, in any order.
* Straight: Five consecutive cards of difrent suits.
* Three of a kind: Three cards of the same rank.
* Two Pair: Two cards of the same rank and two of another.
* One Pair: Two cards of the same rank.
* High Card: Highest card when no other combination is posible.

> Note that the your hand will be flaged as High Card when you do not clasify as any one on top of it.

### Both Playes have the same hand

Sometimes playes can both have the same hand then we need calculate the total of xp each card gives then the player with the highest xp wins. The following xp values corespond to the cards ranking as below:

* A = 1
* 2 = 2xp
* 3 = 3xp
* 4 = 4xp
* 5 = 5xp
* 6 = 6xp
* 7 = 7xp
* 8 = 8xp
* 9 = 9xp
* 10 = 10xp
* J = 10xp
* Q = 12xp
* K = 13xp
* A = 14xp

> In some rare case both playes have the same hands and have the same xp then it will be seen as a tie.