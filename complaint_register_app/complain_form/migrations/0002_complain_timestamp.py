# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complain_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 1, 16, 18, 41, 930000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
