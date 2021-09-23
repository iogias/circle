from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer


class UserApiView(APIView):
    # authentication_classes = (CustomAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    # def get_object(self, wallet_id):
    #     try:
    #         return User.objects.get(username=wallet_id)
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND, data={"data": "Not found"})
    # @swagger_auto_schema(
    #     operation_description='Get User Wallet ID',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['url'],
    #         properties={
    #             'url': openapi.Schema(type=openapi.TYPE_STRING)
    #         },
    #     ),
    #     tags=['UserWalletID'],
    # )
    def get(self, request, wallet_id, format=None):
        if request.method == 'GET':
            if wallet_id is None:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Not found"})
            user = get_object_or_404(User, username=wallet_id)
            if not user:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Not found"})
            serializer = UserSerializer(user)
            return Response(status=status.HTTP_200_OK, data={"detail": serializer.data})


class UserProfileApiView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request, wallet_id, format=None):

        if request.method == 'GET':
            if wallet_id is None:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Not found"})
            user = get_object_or_404(UserProfile, user__username=wallet_id)
            if not user:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Not found"})
            serializer = UserProfileSerializer(user)
            return Response(status=status.HTTP_200_OK, data={"detail": serializer.data})
        else:
            return None
