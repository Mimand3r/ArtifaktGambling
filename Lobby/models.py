from django.db import models


class Lobby(models.Model):

    max_slots = models.IntegerField(default=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('room', args=[str(self.id)])

    def get_all_players(self):
        from steam_auth.models import SteamUser
        return SteamUser.objects.filter(lobby=self)


# TODO LobbyManager der Query für getALlPlayers anbietet
