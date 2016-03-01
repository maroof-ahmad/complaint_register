# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain_form', '0003_auto_20160301_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complain_type',
            field=models.CharField(default=b'Electricity', max_length=50, choices=[(b'Electricity', b'Electricity'), (b'Carpentary', b'Carpentary'), (b'Sanitory', b'Sanitory'), (b'Others', b'Others')]),
        ),
    ]
