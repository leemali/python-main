# deck_of_cards
from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        # return "{} of {}".format(self.value, self.suit)
        return f"{self.value} of {self.suit}"

# c = Card("A", "hearts")
# c2 = Card("10", "Diamonds")
# c3 = Card("K", "Spades")
# print(c, c2, c3)

class Deck:
    def __init__(self):
        suits = ["Heards", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __iter__(self):
        return iter(self.cards)


        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        ## print(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError ("All cards have been dealt")      # print(f"Going to remove {actual} cards.")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only fulldecks can be shuffled")
        shuffle(self.cards)


# d = Deck()
# d.shuffle()
# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# print(d.cards)
# card2 = d.deal_card()


my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
    print(card)



