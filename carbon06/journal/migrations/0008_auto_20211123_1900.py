# Generated by Django 3.2.6 on 2021-11-23 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20211121_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='isWide',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='journal',
            name='article_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 19, 0, 35, 637357)),
        ),
    ]
