# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoliberty', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipioBeneficiado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('populacao', models.FloatField(verbose_name=b'Popula\xc3\xa7\xc3\xa3o')),
                ('populacao_d', models.DateField(verbose_name=b'Data Popula\xc3\xa7\xc3\xa3o')),
                ('pessoas_cadunico', models.FloatField(verbose_name=b'Pessoas Cad\xc3\xbanico')),
                ('pessoas_cadunico_d', models.DateField(verbose_name=b'Data Pessoas Cad\xc3\xbanico')),
                ('familias_cadunico', models.FloatField(verbose_name=b'Familias Cad\xc3\xbanico')),
                ('familias_cadunico_atendidas', models.FloatField(verbose_name=b'Familias Atendidas Cad\xc3\xbanico')),
                ('familias_cadunico_d', models.DateField(verbose_name=b'Data Familias Cad\xc3\xbanico')),
                ('valor_pago', models.FloatField(verbose_name=b'Valor Pago')),
                ('valor_pago_d', models.DateField(verbose_name=b'Data Valor Pago')),
                ('agricultura_familiar', models.FloatField(verbose_name=b'Familias Agricultura Familiar')),
                ('agricultura_familiar_atendidas', models.FloatField(verbose_name=b'Familias Atendidas Agricultura Familiar')),
                ('agricultura_familiar_d', models.DateField(verbose_name=b'Data Familiar Agricultura Familiar')),
                ('idh', models.FloatField(verbose_name=b'\xc3\x8dndice de Desenvolvimento Humano')),
                ('idh_d', models.DateField(verbose_name=b'Data \xc3\x8dndice de Desenvolvimento Humano')),
                ('pib_percapita', models.FloatField(verbose_name=b'PIB Percapita')),
                ('pib_percapita_d', models.DateField(null=True, verbose_name=b'Data PIB Percapita', blank=True)),
                ('pessoas_renda_77', models.FloatField(null=True, verbose_name=b'Renda de at\xc3\xa9 77,00', blank=True)),
                ('pessoas_renda_154', models.FloatField(null=True, verbose_name=b'Renda de 77,01 at\xc3\xa9 154,00', blank=True)),
                ('pessoas_renda_394', models.FloatField(null=True, verbose_name=b'Renda de 154,01 at\xc3\xa9 394,00', blank=True)),
                ('pessoas_renda_acima', models.FloatField(null=True, verbose_name=b'Renda acima de 394,01', blank=True)),
                ('familias_renda_77', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita de at\xc3\xa9 77,00', blank=True)),
                ('familias_renda_154', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita de 77,01 at\xc3\xa9 154,00', blank=True)),
                ('familias_renda_394', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita de 154,01 at\xc3\xa9 394,00', blank=True)),
                ('familias_renda_acima', models.FloatField(null=True, verbose_name=b'Familias Renda Percapita acima de 394,01', blank=True)),
                ('renda_d', models.DateField(null=True, verbose_name=b'Data renda Percapita', blank=True)),
                ('municipio', models.ForeignKey(verbose_name=b'Munic\xc3\xadpio', to='geoliberty.Municipio')),
            ],
            options={
                'verbose_name': 'Municipio Beneficiado',
                'verbose_name_plural': 'Municipios Beneficiados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MunicipioCadUnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('populacao', models.FloatField(verbose_name=b'Popula\xc3\xa7\xc3\xa3o')),
                ('p_cadunico', models.FloatField(verbose_name=b'Popula\xc3\xa7\xc3\xa3o CadUnico')),
                ('f_cadunico', models.FloatField(verbose_name=b'Fam\xc3\xadlias CadUnico')),
                ('f_atendidas_cadunico', models.FloatField(verbose_name=b'Fam\xc3\xadlias Atendidas CadUnico')),
                ('municipio', models.ForeignKey(verbose_name=b'Munic\xc3\xadpio', to='geoliberty.Municipio')),
            ],
            options={
                'verbose_name': 'Municipios CadUnico',
                'verbose_name_plural': 'Municipios CadUnico',
            },
            bases=(models.Model,),
        ),
    ]
