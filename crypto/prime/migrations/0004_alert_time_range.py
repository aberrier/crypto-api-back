# Generated by Django 2.1.5 on 2019-02-04 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0003_remove_alert_time_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='time_range',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
