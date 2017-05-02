from django.test import TestCase
from model_mommy import mommy
from periodo.models import Periodo
from linha.models import Linha, Carro
from datetime import datetime


class TestePeriodo(TestCase):
    def setUp(self):
        self.Linha = mommy.make(Linha, num_linha="971-R", nome_linha="Santana")
        self.carro = mommy.make(Carro, num_carro=3374, observacao="teste")
        self.periodo = mommy.make(Periodo, dataAtual=datetime.today().now(), horario_entrada=datetime.today().time(),
                                  horario_saida=datetime.today().time(), linha=self.Linha, carro=self.carro, folga=False)

    def testar(self):
        self.assertTrue(self.periodo.__str__(),Periodo.dataAtual)