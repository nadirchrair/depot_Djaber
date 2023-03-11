# Generated by Django 4.0.6 on 2023-03-04 19:15

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('DepotApp', '0003_remove_operation_clarque_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='clarque',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='date_depart',
            field=models.DateField(default=datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='prix_de_facture',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]