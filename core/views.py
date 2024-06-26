from django.shortcuts import render, redirect
from django.http import JsonResponse

from game.Table import ShanTable
from .helper import generate_game

# Create your views here.
def home(request):
    for key in request.session.keys():
        request.session[key] = None

    return render(request, 'core/index.html', {})

def play(request):
    if request.method == "POST":
        username = request.POST.get('username')
        request.session["username"] = username
        json = generate_game(username)
        request.session["game"] = json

        return redirect('game')
    return render(request, 'core/play.html', {})

def game(request):
    username = request.session.get('username')
    if not username:
        redirect('play')

    if request.session.get("started") == True:
        username = request.session["username"]
        json = generate_game(username)
        for key in request.session.keys():
            request.session[key] = None
        request.session["username"] = username
        request.session["game"] = json
        return redirect('game')

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
    resp = {}
    if card:
        request.session["taked"] = True
        resp = card.convert_json()
    return JsonResponse({
        'username': username,
        'card': resp
    })

def winners(request):
    json = request.session.get('game')
    username = request.session.get('username')
    if not json and username:
        return JsonResponse({
            'status': "ERROR"
        })
    
    table = ShanTable(None, None)
    table.insert_json(json)
    for user in table.players:
        if user.total < 7 and user.name != username:
            table.take(user)
    
    table.shot()
    json = table.convert_json()
    request.session['game'] = json
    return JsonResponse({
        'username': username,
        'players': [player.convert_json() for player in table.players],
        'winners': [winner.convert_json() for winner in table.winners]
    })
    
