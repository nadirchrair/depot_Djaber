# Generated by Django 4.0.6 on 2023-03-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DepotApp', '0008_alter_operation_date_depart'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='Pallete',
            field=models.FloatField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='clarque',
            field=models.FloatField(blank=True, default=True, null=True),
        ),
    ]
