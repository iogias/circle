from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.html import format_html


class ThemeProfile(models.Model):
    THEME_ATTRIBUTE = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ]
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='users/theme/', blank=True)
    is_active = models.BooleanField(default=True)
    attribute = models.CharField(max_length=8, default='basic', choices=THEME_ATTRIBUTE)

    class Meta:
        verbose_name = 'theme'
        verbose_name_plural = 'themes'

    def __str__(self) -> str:
        return self.name

    def thumbnail(self):
        if self.image:
            return format_html('<img src="{}" style="border-radius:5px;width: 40px;height: 40px"/>'
                               .format(self.image.url))
        else:
            return 'No Image'

    thumbnail.short_description = 'thumbnail'


class UserProfileType(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='users/badge/', blank=True)

    class Meta:
        verbose_name = 'profile type'
        verbose_name_plural = 'profile types'

    def __str__(self) -> str:
        return self.name

    def thumbnail(self):
        if self.icon:
            return format_html('<img src="{}" style="border-radius:5px;width: 40px;height: 40px"/>'
                               .format(self.icon.url))
        else:
            return 'No Image'

    thumbnail.short_description = 'thumbnail'


class UserProfileBadge(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='users/badge/', blank=True)

    class Meta:
        verbose_name = 'profile badge'
        verbose_name_plural = 'profile badges'

    def __str__(self) -> str:
        return self.name

    def thumbnail(self):
        if self.icon:
            return format_html('<img src="{}" style="border-radius:5px;width: 40px;height: 40px"/>'
                               .format(self.icon.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'thumbnail'


class UserProfile(models.Model):
    USER_PROFILE_STATUS = [
        ('active', 'Active'),
        ('banned', 'Banned'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user',
                                on_delete=models.CASCADE, verbose_name='Wallet ID', editable=False)
    # email = models.EmailField(blank=True, unique=True)
    name = models.CharField(max_length=120, blank=True, editable=False)
    display_name = models.CharField(max_length=64, blank=True, null=True)
    profile_img = models.ImageField(upload_to='users/profile', blank=True)
    theme_img = models.ForeignKey(ThemeProfile, on_delete=models.CASCADE, related_name='themes')
    premium = models.BooleanField(default=False, editable=False)
    profile_type = models.ManyToManyField(UserProfileType)
    user_profile_status = models.CharField(max_length=6, default='active', choices=USER_PROFILE_STATUS)
    xp = models.PositiveIntegerField(default=0)
    circle_coins = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def thumbnail(self):
        if self.icon:
            return format_html('<img src="{}" style="border-radius:5px;width: 40px;height: 40px"/>'
                               .format(self.profile_img.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'thumbnail'


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


# post_save.connect(create_profile, sender=User)
