from rest_framework import serializers
from .models import Activitie


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activitie
        field = ['title', 'description','asignee', 'estimation', 'status' ]
