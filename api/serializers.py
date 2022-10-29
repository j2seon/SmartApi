from rest_framework import serializers
from .models import ControlApi

class ControlApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlApi
        fields = ['datetime', 'customer_id', 'flowrate', 'tds', 'ph', 'temp', 'humidity', 'co2', 'do', 'pump', 'led1', 'led2', 'led3']

