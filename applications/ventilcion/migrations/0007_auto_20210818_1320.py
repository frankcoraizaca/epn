# Generated by Django 3.2.6 on 2021-08-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilcion', '0006_auto_20210818_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='d1distancia',
            field=models.FloatField(blank=True, verbose_name='Distancia del tramo[m]'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='de1',
            field=models.CharField(blank=True, max_length=50, verbose_name='Derivación 1'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='de2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Derivación 2'),
        ),
    ]
