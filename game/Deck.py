from .Card import Card
import random

class Deck:
    colors = ['heart', 'diamonds', 'spades', 'clubs']

    def __init__(self, cards=None):
        if cards:
            self.deck = cards
            return
        self.deck = [Card(value, color) for value in range(1,14) for color in self.colors]

    def __len__(self):
        return len(self.deck)

    def randomize(self):
        random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop(-1)
    
    def convert_json(self):
        return [card.convert_json() for card in self.deck]