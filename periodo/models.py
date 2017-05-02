from __future__ import unicode_literals
from django.db import models
from rota.models import Linha, Carro
from .querys import MesQuerySet


class Periodo(models.Model):
    dataAtual = models.DateField(verbose_name=u"Data Atual")
    horario_entrada = models.TimeField(verbose_name=u"Horario de Entrada")
    horario_saida = models.TimeField(verbose_name=u"Horario de Saida")
    linha = models.ForeignKey(Linha, related_name="Linha")
    carro = models.ForeignKey(Carro, related_name="Carro")
    folga = models.BooleanField(verbose_name=u"Folga", default=False)
    total_horas = models.PositiveIntegerField(verbose_name=u"Total", blank=True, null=True)
    objects = MesQuerySet.as_manager()

    def __str__(self):
        return str(self.dataAtual)

    class Meta:
        ordering = ['dataAtual']
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
