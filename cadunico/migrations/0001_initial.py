# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoliberty', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipioCadUnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('populacao', models.IntegerField(verbose_name=b'Popula\xc3\xa7\xc3\xa3o')),
                ('p_cadunico', models.IntegerField(verbose_name=b'Popula\xc3\xa7\xc3\xa3o CadUnico')),
                ('f_cadunico', models.IntegerField(verbose_name=b'Fam\xc3\xadlias CadUnico')),
                ('f_atendidas_cadunico', models.IntegerField(verbose_name=b'Fam\xc3\xadlias Atendidas CadUnico')),
                ('municipio', models.ForeignKey(verbose_name=b'Munic\xc3\xadpio', to='geoliberty.Municipio')),
            ],
            options={
                'verbose_name': 'Municipios CadUnico',
                'verbose_name_plural': 'Municipios CadUnico',
            },
            bases=(models.Model,),
        ),
    ]
