# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadunico', '0006_auto_20151125_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='familias_cadunico',
            field=models.FloatField(null=True, verbose_name=b'Familias Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='familias_cadunico_atendidas',
            field=models.FloatField(null=True, verbose_name=b'Familias Atendidas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='familias_cadunico_d',
            field=models.DateField(null=True, verbose_name=b'Data Familias Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='pessoas_cadunico',
            field=models.FloatField(null=True, verbose_name=b'Pessoas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='pessoas_cadunico_d',
            field=models.DateField(null=True, verbose_name=b'Data Pessoas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='populacao',
            field=models.FloatField(null=True, verbose_name=b'Popula\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='estadobeneficiado',
            name='populacao_d',
            field=models.DateField(null=True, verbose_name=b'Data Popula\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='familias_cadunico',
            field=models.FloatField(null=True, verbose_name=b'Familias Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='familias_cadunico_atendidas',
            field=models.FloatField(null=True, verbose_name=b'Familias Atendidas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='familias_cadunico_d',
            field=models.DateField(null=True, verbose_name=b'Data Familias Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='pessoas_cadunico',
            field=models.FloatField(null=True, verbose_name=b'Pessoas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='pessoas_cadunico_d',
            field=models.DateField(null=True, verbose_name=b'Data Pessoas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='populacao',
            field=models.FloatField(null=True, verbose_name=b'Popula\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='municipiobeneficiado',
            name='populacao_d',
            field=models.DateField(null=True, verbose_name=b'Data Popula\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='familias_cadunico',
            field=models.FloatField(null=True, verbose_name=b'Familias Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='familias_cadunico_atendidas',
            field=models.FloatField(null=True, verbose_name=b'Familias Atendidas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='familias_cadunico_d',
            field=models.DateField(null=True, verbose_name=b'Data Familias Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='pessoas_cadunico',
            field=models.FloatField(null=True, verbose_name=b'Pessoas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='pessoas_cadunico_d',
            field=models.DateField(null=True, verbose_name=b'Data Pessoas Cad\xc3\xbanico', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='populacao',
            field=models.FloatField(null=True, verbose_name=b'Popula\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='paisbeneficiado',
            name='populacao_d',
            field=models.DateField(null=True, verbose_name=b'Data Popula\xc3\xa7\xc3\xa3o', blank=True),
        ),
    ]
