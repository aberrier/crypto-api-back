# Generated by Django 2.1.5 on 2019-02-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0005_alert_last_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='value',
            field=models.PositiveIntegerField(),
        ),
    ]
