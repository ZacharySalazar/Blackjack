import Cards as C
import random
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
suit_list = ["(c)", "(d)", "(h)", "(s)"]

class Deck:
    cards_list = []

    def __init__(self):

        for card_v in card_values:
            for suit in suit_list:
                card_created = C.Card(card_v, suit)
                self.cards_list.append(card_created)

    def shuffle(self):

        for card in self.cards_list:
            random_placement = random.randint(0, len(self.cards_list))
            self.cards_list.remove(card)
            self.cards_list.insert(random_placement, card)


deck = Deck()
full_deck = Deck() #used to refill deck with popped cards between game rounds
deck.shuffle()
