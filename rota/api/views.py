from rest_framework import generics
from .serializers import LinhaSerializer, CarroSerializer
from rota.models import Linha, Carro


class CreateLinha(generics.CreateAPIView):
    serializer_class = LinhaSerializer
    queryset = Linha.objects.all()


class Linhas(generics.ListAPIView):
    serializer_class = LinhaSerializer
    queryset = Linha.objects.all()


class Linha(generics.RetrieveAPIView):
    serializer_class = LinhaSerializer
    queryset = Linha.objects.all()
    lookup_field = 'id'


class CreateCarro(generics.CreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


class Carros(generics.ListAPIView):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()


class Carro(generics.RetrieveAPIView):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()
    lookup_field = 'id'


