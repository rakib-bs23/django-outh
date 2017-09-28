from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ObItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ObItem
        fields = ('item_code','item_description_english')