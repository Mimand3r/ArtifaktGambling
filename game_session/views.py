from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GameSession


# Create a new Game
def newGame(request):
    # Erzeuge neue GameSession
    new_game = GameSession()
    new_game.save()
    # Adde Spieler zur GameListe
    new_game.add_player(request.user)
    # Redirect to Game
    return redirect('main_page')  # TODO redirect to gamePage


# Show Specific Game
def Game(request):
    pass

# TODO Leave Game

# TODO JoinExistingGame

