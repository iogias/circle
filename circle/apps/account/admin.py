from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (ThemeProfile, UserProfile, UserProfileBadge,
                     UserProfileType)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('name__istartswith',)
    list_display = ('name', 'user', 'premium')
    list_filter = ('premium',)
    list_per_page = 10


@admin.register(UserProfileType)
class UserProfileTypeAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'description', 'is_active', )
    list_editable = ('is_active',)
    readonly_fields = ('thumbnail',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(UserProfileBadge)
class UserProfileBadgeAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'description', 'is_active')
    list_editable = ('is_active',)
    readonly_fields = ('thumbnail',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ThemeProfile)
class ThemeProfileAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'attribute', 'is_active', )
    list_editable = ('is_active',)
    readonly_fields = ('thumbnail',)
    prepopulated_fields = {'slug': ('name',)}


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'profile_name', 'premium', 'is_active',)
    list_per_page = 10
    list_filter = ('is_active', 'groups',)

    @admin.display(ordering='user__name')
    def profile_name(self, obj):
        return obj.user.name

    @admin.display(boolean=True)
    def premium(self, obj):
        return obj.user.premium


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
