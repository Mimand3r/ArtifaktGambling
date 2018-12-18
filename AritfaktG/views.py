from django.contrib.auth.views import auth_logout
from django.shortcuts import render, redirect
from django.views import View
from Lobby.models import Lobby


def main_page(request):

    # Konstruiere All Lobbys Query
    lobbies = Lobby.objects.all()

    return render(request, 'main_page.html', {'lobbies': lobbies})


