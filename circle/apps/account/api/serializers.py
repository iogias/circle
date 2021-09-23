from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import (ThemeProfile, UserProfile, UserProfileBadge,
                      UserProfileType)


class UserProfileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileType
        fields = '__all__'


class UserProfileBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileBadge
        fields = '__all__'


class ThemeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeProfile
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['theme_img'] = ThemeProfileSerializer(instance.theme_img).data

        return response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
