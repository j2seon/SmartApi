
from rest_framework import serializers
from .models import LastData


class LastDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastData
        fields = ('datetime', 'customer_id', 'flowrate', 'tds', 'ph', 'temp', 'humidity', 'co2', 'do', 'pump', 'led1', 'led2', 'led3')

