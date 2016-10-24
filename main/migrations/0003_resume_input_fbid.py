# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_resume_input_greetings'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_input',
            name='fbid',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
