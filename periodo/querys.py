from __future__ import unicode_literals
from django.db import models


class MesQuerySet(models.query.QuerySet):

    def periodoAnoMes(self, mes, ano):
        return self.filter(dataAtual__month=mes, dataAtual__year=ano)


