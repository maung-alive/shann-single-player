from game.Card import Card
from game.Table import ShanTable
from game.Player import Player
from game.Computer import Computer

def generate_game(username):
    players = []
    player = Player(username)
    players.append(player)
    for i in range(1, 5):
        computer = Computer("Computer " + str(i))
        players.append(computer)

    colors = ['heart', 'diamonds', 'spades', 'clubs']
    table = ShanTable(players=players, deck=[Card(value, color) for value in range(1,14) for color in colors])
    json = table.convert_json()
    return json
