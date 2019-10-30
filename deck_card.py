# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [x] build card
# [x] build deck
# [x] implement shuffle
# [x] implement a sort
# [ ] implement a game

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        self.name = names.get(value) or str(value)

    def show_value(self):
        print(f"{self.name} of {self.suit}")


# ace_of_hearts = Card('hearts', 1)
# ace_of_hearts.show_value()


class Deck:
    def __init__(self):
        self.cards = []

        # populate / the cards list
        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            # build each suit
            for value in range(1, 14):
                # create a card
                self.cards.append(Card(suit, value))

    def shuffle(self):
        for card in range(len(self.cards) - 1, -1, -1):
          random_index = random.randint(0, len(self.cards) - 1)
          self.cards[card], self.cards[random_index] = self.cards[random_index], self.cards[card]
        return self

    def sort(self):
        self.cards.sort(key=lambda cards: (cards.suit, cards.value))
        return self
# blackjack game
    def game(self):
        pass


bicycle_deck = Deck()
bicycle_deck.shuffle().sort()
for card in bicycle_deck.cards:
    card.show_value()


