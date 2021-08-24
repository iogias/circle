from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('name__startswith', )
    list_display = ('img', 'user', 'name', 'premium')
    list_filter = ('premium',)
    list_per_page = 10


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'profile_name', 'premium', 'is_active',)
    list_per_page = 10
    list_filter = ('profile__premium', 'is_active', 'groups',)

    @admin.display(ordering='profile__name')
    def profile_name(self, obj):
        return obj.profile.name

    @admin.display(boolean=True)
    def premium(self, obj):
        return obj.profile.premium


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
