# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_auto_20160524_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='resumo',
            field=models.FileField(null=True, upload_to=b'/home/paulo/projetos/grupo-gestao-org/geoliberty/assets/geoliberty/assests/files/resumos-workshop'),
            preserve_default=True,
        ),
    ]
