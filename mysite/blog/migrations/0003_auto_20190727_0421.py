# Generated by Django 2.1 on 2019-07-26 22:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190727_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 26, 22, 51, 9, 289412, tzinfo=utc)),
        ),
    ]
