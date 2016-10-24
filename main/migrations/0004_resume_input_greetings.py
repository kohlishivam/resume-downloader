# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_resume_input_fbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_input',
            name='greetings',
            field=models.CharField(max_length=250, null=True),
            preserve_default=True,
        ),
    ]
