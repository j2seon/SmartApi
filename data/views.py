from django.shortcuts import render
from rest_framework import viewsets

from data.models import LastData
from data.serializers import LastDataSerializer


# Create your views here.
# Create your views here.
class LastDataViewSet(viewsets.ModelViewSet):
    queryset = LastData.objects.all()
    serializer_class = LastDataSerializer