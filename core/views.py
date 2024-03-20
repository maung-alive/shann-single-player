from django.shortcuts import render

from game.Player import Player
from game.Computer import Computer
from game.Table import ShanTable
from game.Deck import Deck

# Create your views here.
def home(request):
    return render(request, 'core/index.html', {})

def play(request):
    if request.method == "POST":
        username = request.POST.get('username')
        request.session["username"] = username
        players = []
        player = Player(username)
        players.append(player)
        for i in range(6):
            computer = Computer("Computer " + str(i))
            players.append(computer)
        
        table = ShanTable(players, Deck())
        json = table.convert_json()
        print(json)
        request.session["game"] = json

        return render(request, 'core/play.html', {})
    return render(request, 'core/play.html', {})