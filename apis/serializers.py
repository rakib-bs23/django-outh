from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ObItem, ResUsers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ObItem
        fields = ('item_code','item_description_english')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SerializerMethodField('get_alternate_name')

    class Meta:
        model = ResUsers
        fields = ('id','login','username','first_name','last_name','role_in_org','mobile','phone','active','is_prime','is_deleted')

    def get_alternate_name(self, obj):
        return obj.user_name