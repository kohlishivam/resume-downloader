# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20161028_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_input',
            name='educational_qualifications_1',
            field=models.CharField(default=datetime.date(2016, 10, 28), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='educational_qualifications_2',
            field=models.CharField(default=datetime.date(2016, 10, 28), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='educational_qualifications_3',
            field=models.CharField(default=datetime.date(2016, 10, 28), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='educational_qualifications_4',
            field=models.CharField(default=datetime.date(2016, 10, 28), max_length=100),
            preserve_default=False,
        ),
    ]
