# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 22:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 16, 22, 32, 7, 102904, tzinfo=utc)),
        ),
    ]