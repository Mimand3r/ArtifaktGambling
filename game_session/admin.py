from django.contrib import admin

# Register your models here.
from .models import GameSession


@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('get_players',)


