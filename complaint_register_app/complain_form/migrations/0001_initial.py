# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('complain_text', models.TextField(max_length=200)),
                ('complain_type', models.CharField(default=b'EE', max_length=2, choices=[(b'EE', b'Electricity'), (b'CP', b'Carpentary'), (b'ST', b'Sanitory'), (b'OT', b'Others')])),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('room_no', models.CharField(max_length=5)),
            ],
        ),
    ]
