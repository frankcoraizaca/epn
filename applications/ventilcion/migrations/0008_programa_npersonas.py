# Generated by Django 3.2.6 on 2021-08-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilcion', '0007_auto_20210818_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='npersonas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de personas'),
        ),
    ]
