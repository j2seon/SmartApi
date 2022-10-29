from django.db import models

# Create your models here.
class ControlApi(models.Model):
    datetime = models.DateTimeField(0)
    customer_id = models.IntegerField()
    flowrate = models.FloatField()
    tds = models.FloatField()
    ph = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()
    co2 = models.FloatField()
    do = models.FloatField()
    pump = models.IntegerField()
    led1 = models.IntegerField()
    led2 = models.IntegerField()
    led3 = models.IntegerField()