# Generated by Django 3.2.3 on 2021-08-18 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20210816_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='article_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 17, 5, 29, 282378)),
        ),
    ]
