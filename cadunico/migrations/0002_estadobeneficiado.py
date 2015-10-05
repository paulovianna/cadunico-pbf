# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoliberty', '__first__'),
        ('cadunico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoBeneficiado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('populacao', models.FloatField(verbose_name=b'Popula\xc3\xa7\xc3\xa3o')),
                ('populacao_d', models.DateField(verbose_name=b'Data Popula\xc3\xa7\xc3\xa3o')),
                ('pessoas_cadunico', models.FloatField(verbose_name=b'Pessoas Cad\xc3\xbanico')),
                ('pessoas_cadunico_d', models.DateField(verbose_name=b'Data Pessoas Cad\xc3\xbanico')),
                ('familias_cadunico', models.FloatField(verbose_name=b'Familias Cad\xc3\xbanico')),
                ('familias_cadunico_atendidas', models.FloatField(verbose_name=b'Familias Atendidas Cad\xc3\xbanico')),
                ('familias_cadunico_d', models.DateField(verbose_name=b'Data Familias Cad\xc3\xbanico')),
                ('pessoas_renda_77', models.FloatField(null=True, verbose_name=b'Renda de at\xc3\xa9 77,00', blank=True)),
                ('pessoas_renda_154', models.FloatField(null=True, verbose_name=b'Renda de 77,01 at\xc3\xa9 154,00', blank=True)),
                ('pessoas_renda_394', models.FloatField(null=True, verbose_name=b'Renda de 154,01 at\xc3\xa9 394,00', blank=True)),
                ('pessoas_renda_acima', models.FloatField(null=True, verbose_name=b'Renda acima de 394,01', blank=True)),
                ('familias_renda_77', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita de at\xc3\xa9 77,00', blank=True)),
                ('familias_renda_154', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita de 77,01 at\xc3\xa9 154,00', blank=True)),
                ('familias_renda_394', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita de 154,01 at\xc3\xa9 394,00', blank=True)),
                ('familias_renda_acima', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita acima de 394,01', blank=True)),
                ('estado', models.ForeignKey(verbose_name=b'Estado', to='geoliberty.Uf')),
            ],
            options={
                'verbose_name': 'Estado Beneficiado',
                'verbose_name_plural': 'Estados Beneficiados',
            },
            bases=(models.Model,),
        ),
    ]
