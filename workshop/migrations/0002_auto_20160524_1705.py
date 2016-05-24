# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='resumo',
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='area',
            field=models.CharField(default=b'GOR', max_length=8, verbose_name=b'\xc3\x81rea Tem\xc3\xa1tica', choices=[(b'GOR', b'Gest\xc3\xa3o e organiza\xc3\xa7\xc3\xa3o rural'), (b'DS', b'Desenvolvimento sustent\xc3\xa1vel'), (b'GM', b'Gest\xc3\xa3o mercadol\xc3\xb3gica')]),
        ),
    ]
