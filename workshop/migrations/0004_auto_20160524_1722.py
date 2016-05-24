# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0003_inscricao_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='resumo',
            field=models.FileField(max_length=256, null=True, upload_to=b'/home/paulo/projetos/grupo-gestao-org/geoliberty/assets/geoliberty/assests/files/resumos-workshop'),
        ),
    ]
