from django.shortcuts import render
from .models import Activitie
from django.views.generic import ListView
from rest_framework import viewsets
from .serializer import ActivitySerializer
from users.models import User
# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ActivitySerializer
class Activity_List(ListView):
    model = Activitie