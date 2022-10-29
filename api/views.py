from django.shortcuts import render
from rest_framework import viewsets

from api.models import ControlApi
from api.serializers import ControlApiSerializer


# Create your views here.
class ControlApiViewSet(viewsets.ModelViewSet):
    queryset = ControlApi.objects.all()
    serializer_class = ControlApiSerializer