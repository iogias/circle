from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Wallet ID')
    # wallet_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120, blank=True)
    img = models.ImageField(upload_to='users/', blank=True)
    premium = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return f'Name {self.name}'
