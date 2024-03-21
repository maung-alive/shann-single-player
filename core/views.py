from django.shortcuts import render, redirect
from django.http import JsonResponse

from game.Player import Player
from game.Computer import Computer
from game.Table import ShanTable
from game.Deck import Deck

# Create your views here.
def home(request):
    for key in request.session.keys():
        request.session[key] = None

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

    if request.session.get("started") == True:
        return redirect('home')
    json = request.session["game"]
    table = ShanTable(None, None)
    table.insert_json(json)
    table.start()
    json = table.convert_json()
    for player in json['players']:
        if player['name'] != username:
            for card in player['cards']:
                card['img'] = "../back.png"
    
    request.session["game"] = json
    request.session["started"] = True
    return render(request, 'core/game.html', {
        'username': username,
        "game": json
    })

def take(request):
    json = request.session.get('game')
    username = request.session.get('username')
    taked = request.session.get("taked")
    if taked == True:
        return JsonResponse({
           'status': "ERROR"
        })
    
    if not json and username:
        return JsonResponse({
            'status': "ERROR"
        })
    table = ShanTable(None, None)
    table.insert_json(json)
    i=0
    for user in json['players']:
        if user['name'] == username:
            break
        i += 1
    card = table.take(table.players[i])
    json = table.convert_json()
    request.session['game'] = json
    resp = card.convert_json()
    request.session["taked"] = True
    return JsonResponse({
        'username': username,
        'card': resp
    })