# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=128, verbose_name=b'T\xc3\xadtulo do Trabalho')),
                ('instituicao', models.CharField(max_length=64, verbose_name=b'Institui\xc3\xa7\xc3\xa3o')),
                ('orientador', models.CharField(max_length=128, verbose_name=b'Orientador')),
                ('participantes', models.TextField(verbose_name=b'Participantes')),
                ('resumo', models.FileField(upload_to=b'/geoliberty/assests/files/resumos-workshop')),
                ('area', models.CharField(max_length=32, verbose_name=b'\xc3\x81rea Tem\xc3\xa1tica', choices=[(b'Gest\xc3\xa3o e organiza\xc3\xa7\xc3\xa3o rural', b'Gest\xc3\xa3o e organiza\xc3\xa7\xc3\xa3o rural'), (b'Desenvolvimento sustent\xc3\xa1vel', b'Desenvolvimento sustent\xc3\xa1vel'), (b'Gest\xc3\xa3o mercadol\xc3\xb3gica', b'Gest\xc3\xa3o mercadol\xc3\xb3gica')])),
            ],
            options={
                'verbose_name': 'Inscri\xe7\xe3o',
                'verbose_name_plural': 'Inscri\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
    ]
