from django.db import models
from steam_auth.models import SteamUser


class GameSession(models.Model):

    SpielerListe = models.ManyToManyField(SteamUser, related_name="player_list")
    has_started = models.BooleanField(default=False)

    # Timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def add_player(self, steam_user):
        self.SpielerListe.add(steam_user)

    def make_rolls(self):
        pass

    # Dienstleistung für admin
    def get_players(self):
        return ','.join([p.personaname for p in self.SpielerListe.all()])

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('people.views.details', args=[str(self.id)])
