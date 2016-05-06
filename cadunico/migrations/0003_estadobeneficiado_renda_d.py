# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadunico', '0002_estadobeneficiado'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadobeneficiado',
            name='renda_d',
            field=models.DateField(null=True, verbose_name=b'Data renda Percapita', blank=True),
            preserve_default=True,
        ),
    ]
