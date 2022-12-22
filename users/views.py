from django.shortcuts import render
from .models import User,UserProfile
from django.views.generic import ListView
from rest_framework import viewsets
from .serializers import UserSerializer, UserProfileSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class User_List(ListView):
    model = User