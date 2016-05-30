# -*- coding: utf-8 -*-
from django.db import models
from geoliberty.settings import MEDIA_ROOT


class Inscricao(models.Model):

    OPCOES = (
        ('GOR', 'Gestão e organização rural'),
        ('DS', 'Desenvolvimento sustentável'),
        ('GM', 'Gestão mercadológica'),
    )

    titulo = models.CharField('Título do Trabalho',max_length=128)
    instituicao = models.CharField('Instituição',max_length=64)
    orientador = models.CharField('Orientador',max_length=128)
    participantes = models.TextField('Participantes')
    resumo = models.FileField(max_length=256, upload_to= 'files/resumos-workshop',null=True)
    area = models.CharField('Área Temática',max_length=8,choices=OPCOES,default='GOR')

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"

    def __unicode__(self):
        return self.titulo