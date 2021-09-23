from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from circle.apps.core.models import CoreBaseModel
from circle.apps.partner.models import Partner


class Game(CoreBaseModel):
    PLATFORM = [
        ('mobile', 'Mobile'),
        ('pc', 'PC'),
    ]
    PVP = [
        ('team', 'Team'),
        ('solo', 'Solo'),
        ('hybrid', 'Hybrid'),
    ]
    platform = models.CharField(max_length=6, choices=PLATFORM, default='mobile')
    pvp = models.CharField(max_length=6, choices=PVP, default='team')
    logo_img = models.ImageField(upload_to='game/', blank=True)
    min_players = models.PositiveSmallIntegerField(blank=False, default=5, verbose_name='Main Player')
    bak_players = models.PositiveSmallIntegerField(blank=False, default=2, verbose_name='Backup Player')

    class Meta:
        ordering = ('name',)
        verbose_name = 'game'
        verbose_name_plural = 'games'


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userid_game = models.CharField(max_length=64, null=False, blank=False, unique=True)
    nickname_game = models.CharField(max_length=80, null=False, blank=False, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='players')

    class Meta:
        ordering = ('user',)
        verbose_name = 'player'
        verbose_name_plural = 'players'


class Team(CoreBaseModel):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=80, blank=True)
    logo_image = models.ImageField(upload_to='team/', blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='teams')

    class Meta:
        ordering = ('name',)
        verbose_name = 'team'
        verbose_name_plural = 'teams'
