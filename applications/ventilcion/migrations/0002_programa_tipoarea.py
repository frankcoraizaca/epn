# Generated by Django 3.2.6 on 2021-08-18 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
        ('ventilcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='tipoarea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.areaslista'),
        ),
    ]
