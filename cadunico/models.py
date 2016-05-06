# -*- coding: utf-8 -*-
from django.db import models
from geoliberty.models import Municipio, Uf, Pais

class MunicipioCadUnico(models.Model):

    municipio = models.ForeignKey(Municipio, verbose_name='Município')
    populacao = models.FloatField('População')
    p_cadunico = models.FloatField('População CadUnico')
    f_cadunico = models.FloatField('Famílias CadUnico')
    f_atendidas_cadunico = models.FloatField('Famílias Atendidas CadUnico')

    class Meta:
        verbose_name = u'Municipios CadUnico'
        verbose_name_plural = u'Municipios CadUnico'

    def __unicode__(self):
        return self.municipio.municipio

    def porc_populacao_cadunico(self):
        return (int)((self.p_cadunico/self.populacao)*100)
    
    def porc_f_atendidas(self):
        return (int)((self.f_atendidas_cadunico/self.f_cadunico)*100)

class Beneficiado(models.Model):

    class Meta:
        abstract = True

    populacao = models.FloatField('População', blank=True, null=True)
    populacao_d = models.DateField('Data População', blank=True, null=True)
    pessoas_cadunico = models.FloatField('Pessoas Cadúnico', blank=True, null=True)
    pessoas_cadunico_d = models.DateField('Data Pessoas Cadúnico', blank=True, null=True)
    familias_cadunico = models.FloatField('Familias Cadúnico', blank=True, null=True)
    familias_cadunico_atendidas = models.FloatField('Familias Atendidas Cadúnico', blank=True, null=True)
    familias_cadunico_d = models.DateField('Data Familias Cadúnico', blank=True, null=True)
    pessoas_renda_77 = models.FloatField('Renda de até 77,00', blank=True, null=True)
    pessoas_renda_154 = models.FloatField('Renda de 77,01 até 154,00', blank=True, null=True)
    pessoas_renda_394 = models.FloatField('Renda de 154,01 até 394,00', blank=True, null=True)
    pessoas_renda_acima = models.FloatField('Renda acima de 394,01', blank=True, null=True)
    familias_renda_77 = models.FloatField('Familias Renda Percapita de até 77,00', blank=True, null=True)
    familias_renda_154 = models.FloatField('Familias Renda Percapita de 77,01 até 154,00', blank=True, null=True)
    familias_renda_394 = models.FloatField('Familias Renda Percapita de 154,01 até 394,00', blank=True, null=True)
    familias_renda_acima = models.FloatField('Familias Renda Percapita acima de 394,01', blank=True, null=True)
    renda_d = models.DateField('Data renda Percapita', blank=True, null=True)

    def porc_pessoas_cadastradas(self):
        return (self.pessoas_cadunico/self.populacao)*100

    def porc_pessoas_atendidas(self):
        pessoas_familia = self.pessoas_cadunico/self.familias_cadunico
        pessoas_atendidas = self.familias_cadunico_atendidas * pessoas_familia
        return (pessoas_atendidas/self.populacao)*100

    def porc_familias_atendidas(self):
        return (self.familias_cadunico_atendidas/self.familias_cadunico)*100

    def porc_familias_cadastradas_77(self):
        return (self.familias_renda_77/self.familias_cadunico)*100

    def porc_familias_cadastradas_154(self):
        return (self.familias_renda_154/self.familias_cadunico)*100

    def porc_familias_cadastradas_394(self):
        return (self.familias_renda_394/self.familias_cadunico)*100

    def porc_familias_cadastradas_acima(self):
        return (self.familias_renda_acima/self.familias_cadunico)*100

    def porc_pessoas_77(self):
        return (self.pessoas_renda_77/self.populacao)*100

    def porc_pessoas_154(self):
        return (self.pessoas_renda_154/self.populacao)*100

    def porc_pessoas_394(self):
        return (self.pessoas_renda_394/self.populacao)*100

    def porc_pessoas_acima(self):
        return (self.pessoas_renda_acima/self.populacao)*100


class MunicipioBeneficiado(Beneficiado):

    class Meta:
        verbose_name = "Municipio Beneficiado"
        verbose_name_plural = "Municipios Beneficiados"

    municipio = models.ForeignKey(Municipio, verbose_name='Município')
    valor_pago = models.FloatField('Valor Pago')
    valor_pago_d = models.DateField('Data Valor Pago')
    agricultura_familiar = models.FloatField('Familias Agricultura Familiar')
    agricultura_familiar_atendidas = models.FloatField('Familias Atendidas Agricultura Familiar')
    agricultura_familiar_d = models.DateField('Data Familiar Agricultura Familiar')
    idh = models.FloatField('Índice de Desenvolvimento Humano')
    idh_d = models.DateField('Data Índice de Desenvolvimento Humano')
    pib_percapita = models.FloatField('PIB Percapita')
    pib_percapita_d = models.DateField('Data PIB Percapita', blank=True, null=True)

    def __unicode__(self):
        return self.municipio.municipio

    def beneficio_medio_familia(self):
        return (self.valor_pago/self.familias_cadunico_atendidas)


class EstadoBeneficiado(Beneficiado):
    class Meta:
        verbose_name = "Estado Beneficiado"
        verbose_name_plural = "Estados Beneficiados"

    estado = models.ForeignKey(Uf, verbose_name='Estado')
    valor_pago = models.FloatField('Valor Pago', blank=True, null=True)
    valor_pago_d = models.DateField('Data Valor Pago', blank=True, null=True)

    def __unicode__(self):
        return self.estado.uf

class PaisBeneficiado(Beneficiado):
    class Meta:
        verbose_name = "País Beneficiado"
        verbose_name_plural = "Países Beneficiados"

    pais = models.ForeignKey(Pais, verbose_name='País')

    def __unicode__(self):
        return self.pais.pais