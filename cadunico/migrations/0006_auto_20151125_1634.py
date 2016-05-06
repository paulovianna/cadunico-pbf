# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadunico', '0005_municipiobeneficiado_pib_percapita_d'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadobeneficiado',
            name='valor_pago',
            field=models.FloatField(null=True, verbose_name=b'Valor Pago', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estadobeneficiado',
            name='valor_pago_d',
            field=models.DateField(null=True, verbose_name=b'Data Valor Pago', blank=True),
            preserve_default=True,
        ),
    ]
