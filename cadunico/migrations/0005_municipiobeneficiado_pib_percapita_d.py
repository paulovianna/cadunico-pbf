# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadunico', '0004_auto_20151005_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipiobeneficiado',
            name='pib_percapita_d',
            field=models.DateField(null=True, verbose_name=b'Data PIB Percapita', blank=True),
            preserve_default=True,
        ),
    ]
