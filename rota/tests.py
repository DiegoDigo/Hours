from django.test import TestCase
from model_mommy import mommy
from .models import Linha, Carro


class TesteLinha(TestCase):

    def setUp(self):
        self.Linha = mommy.make(Linha, num_linha="971-R", nome_linha="Santana")

    def testar(self):
        self.assertTrue(self.Linha.__str__(), Linha.num_linha)


class TesteCarro(TestCase):

    def setUp(self):
        self.carro = mommy.make(Carro, num_carro=3374, observacao="teste")

    def testar(self):
        self.assertTrue(self.carro.__str__(), Carro.num_carro)