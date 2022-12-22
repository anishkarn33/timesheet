from rest_framework import serializers
from .models import UserProfile,User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', )


class UserProfileSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)
    is_email_verified = serializers.BooleanField(source='user.is_email_verified', read_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ('id', ' first_name', 'last_name', 'avatar', 'is_active', 'is_email_verified', 'email',)

    def update(self,instance,validated_data):
        try:
           if instance.email != None:
            email = validated_data.pop('email',None)

        except KeyError:
            pass