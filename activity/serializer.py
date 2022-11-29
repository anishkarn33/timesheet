from rest_framework import serializers
from .models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = User
        field = ['id', 'name', 'email', 'is_staff', 'url' ]
