# Generated by Django 4.1 on 2022-10-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ControlApi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField(verbose_name=0)),
                ("customer_id", models.IntegerField()),
                ("flowrate", models.FloatField()),
                ("tds", models.FloatField()),
                ("ph", models.FloatField()),
                ("temp", models.FloatField()),
                ("humidity", models.FloatField()),
                ("co2", models.FloatField()),
                ("do", models.FloatField()),
                ("pump", models.IntegerField()),
                ("led1", models.IntegerField()),
                ("led2", models.IntegerField()),
                ("led3", models.IntegerField()),
            ],
        ),
    ]
