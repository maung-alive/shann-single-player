from .Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total = 0
        self.power = False

    def __check_null(self, total):
        while total > 10:
            total -= 10
        return total

    def __check_power(self):
        color = ''
        for card in self.cards:
            if card.color == color:
                self.power = True
            else:
                self.power = False
            color = card.color

    def __add_cards(self):
        i = 0
        for card in self.cards:
            if card.value in [11, 12, 13]:
                i += 0
            else:
                i += card.value

        if i == 10:
            i = 0

        i = self.__check_null(i)
        self.total = i

    def receive(self, card):
        self.cards.append(card)
        self.__add_cards()
        self.__check_power()
    
    def convert_json(self):
        return {
            'name': self.name,
            'cards': [card.convert_json() for card in self.cards],
            'total': self.total,
            'power': self.power
        }
    
    def insert_json(self, json):
        self.name = json['name']
        self.cards = [Card(card['value'], card['color']) for card in json['cards']]
        self.total = json['total']
        self.power = json['power']