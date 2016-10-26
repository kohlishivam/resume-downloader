# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_resume_input_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_input',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='emailid',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='fbid',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='greetings',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='state',
            field=models.CharField(max_length=1000),
        ),
    ]
