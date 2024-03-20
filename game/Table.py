class ShanTable:
    def __init__(self, players, deck):
        self.taken_players = []
        self.players = players
        self.deck = deck
        self.winners = []

    def start(self):
        self.deck.randomize()
        for i in range(2):
            for player in self.players:
                card = self.deck.pop()
                player.receive(card)

    def take(self, player):
        if player not in self.taken_players:
            card = self.deck.pop()
            player.receive(card)
            self.taken_players.append(player)
            return card
        return False

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
        return self.winnersclass ShanTable:
    def __init__(self, players, deck):
        self.taken_players = []
        self.players = players
        self.deck = deck
        self.winners = []

    def start(self):
        self.deck.randomize()
        for i in range(2):
            for player in self.players:
                card = self.deck.pop()
                player.receive(card)

    def take(self, player):
        if player not in self.taken_players:
            card = self.deck.pop()
            player.receive(card)
            self.taken_players.append(player)
            return card
        return False

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