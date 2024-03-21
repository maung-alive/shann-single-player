from .Card import Card
from .Player import Player
from .Deck import Deck

class ShanTable:
    def __init__(self, players, deck):
        self.taken_players = []
        self.players = players
        self.deck = deck
        self.winners = []

    def start(self):
        self.deck.randomize()
        for player in self.players:
            if len(player.cards) < 2:
                player.receive(self.deck.pop())
                player.receive(self.deck.pop())

    def take(self, player):
        if len(player.cards) < 3:
            card = self.deck.pop()
            player.receive(card)
            self.taken_players.append(player)
            return card
        return None

    def shot(self):
        winner = self.players[0]

        for player in self.players[1:]:
            if winner.total == player.total:
                if winner.power is True and player.power is True:
                    self.winners.append(winner)
                    self.winners.append(player)
                elif winner.power is True:
                    pass
                elif player.power is True:
                    winner = player
                else:
                    self.winners.append(winner)
                    self.winners.append(player)
            elif winner.total > player.total:
                pass
            elif winner.total < player.total:
                winner = player

        self.winners.append(winner)
        return self.winners
    
    def convert_json(self):
        return {
            'taken_players': [player.convert_json() for player in self.taken_players],
            'deck': self.deck.convert_json(),
            'winners': [winner.convert_json() for winner in self.winners],
            'players': [player.convert_json() for player in self.players]
        }
    
    def insert_json(self, json):
        self.taken_players = [Player(player['name']) for player in json['taken_players']]
        self.deck = Deck([Card(card['value'], card['color']) for card in json['deck']])
        self.winners = [Player(winner['name']) for winner in json['winners']]
        self.players = [Player(player['name']) for player in json['players']]