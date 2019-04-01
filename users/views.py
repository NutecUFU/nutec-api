from django.shortcuts import render
from rest_framework import viewsets
from users.serializers import UserSerializer
from rest_framework import permissions
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)
    