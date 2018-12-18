from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Lobby


@login_required
def join_lobby(request, id):
    # GetObject via ID
    lobby = get_object_or_404(Lobby, id=id)
    request.user.lobby = lobby
    request.user.save()
    return redirect(lobby)  # todo redirect to lobby-page


@login_required
def leave_lobby(request):
    request.user.lobby = None
    request.user.save()
    return redirect("home")


@login_required
def room(request, id):
    try:
        lobby = get_object_or_404(Lobby, id=id)
    except:
        return redirect('home')
    players = lobby.get_all_players()
    user_is_in_lobby = players.filter(id=request.user.id).exists()
    return render(request, 'Lobby/room.html', {'lobby': lobby,
                                               'players': players,
                                               'user_is_in_lobby': user_is_in_lobby})

