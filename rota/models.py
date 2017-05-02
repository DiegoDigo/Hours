from __future__ import unicode_literals
from django.db import models
from .querys import QuerySetVeiculo


class Carro(models.Model):
    num_carro = models.PositiveIntegerField(verbose_name=u"Número carro")
    observacao = models.TextField(verbose_name=u"Observações", blank=True, null=True)
    objects = QuerySetVeiculo.as_manager()

    def __str__(self):
        return str(self.num_carro)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        ordering = ["num_carro"]


class Linha(models.Model):
    num_linha = models.CharField(verbose_name=u"Linha do veiculo", max_length=10)
    nome_linha = models.CharField(verbose_name=u"Nome da linha", max_length=100)

    def __str__(self):
        return self.nome_linha

    class Meta:
        verbose_name = "Linha"
        verbose_name_plural = "Linhas"
        ordering = ["num_linha"]