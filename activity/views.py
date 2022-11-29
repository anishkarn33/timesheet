from django.shortcuts import render
from .models import Activitie
from django.views.generic import ListView
# Create your views here.


class Activity_List(ListView):
    model = Activitie