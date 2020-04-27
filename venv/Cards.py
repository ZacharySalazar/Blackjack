import random

class Card:
    def __init__(self, card_id, suit):
        self.card_id = card_id
        self.suit = suit

        try:
            if  self.card_id == int(card_id):
                self.value =  self.card_id
                self.title = str( self.card_id) + self.suit

        except ValueError:
            self.value = 10
            self.title = card_id + self.suit
            self.suit = self.suit




