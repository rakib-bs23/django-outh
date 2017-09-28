# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, UsersSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .models import ObItem, ResUsers

class UserViewSet(viewsets.ModelViewSet):
    """
    Return a list of all the existing users.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        Return a list of all item codes.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['drivers']
    queryset = ObItem.objects.all()
    serializer_class = GroupSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """
        Return a list of all system users.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['drivers']
    queryset = ResUsers.objects.all()
    serializer_class = UsersSerializer