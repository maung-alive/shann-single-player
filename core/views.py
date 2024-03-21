from django.shortcuts import render, redirect

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
        for i in range(1, 5):
            computer = Computer("Computer " + str(i))
            players.append(computer)
        
        table = ShanTable(players, Deck())
        json = table.convert_json()
        request.session["game"] = json

        return redirect('game')
    return render(request, 'core/play.html', {})

def game(request):
    username = request.session.get('username')
    if not username:
        redirect('play')
    json = request.session["game"]
    table = ShanTable(None, None)
    table.insert_json(json)
    table.start()
    json = table.convert_json()
    request.session["game"] = json
    for player in json['players']:
        if player['name'] != username:
            for card in player['cards']:
                card['img'] = "../back.png"
    print(json)
    
    return render(request, 'core/game.html', {
        'username': username,
        "game": json
    })