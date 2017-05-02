from rest_framework import generics
from .serializers import PeriodoSerializer, CreatePeriodoSerializer
from periodo.models import Periodo


class CreateDia(generics.CreateAPIView):
    serializer_class = CreatePeriodoSerializer
    queryset = Periodo.objects.all()


class Dia(generics.RetrieveAPIView):
    serializer_class = PeriodoSerializer
    queryset = Periodo.objects.all()
    lookup_field = 'id'


class Dias(generics.ListAPIView):
    serializer_class = PeriodoSerializer

    def get_queryset(self):
        return Periodo.objects.periodoAnoMes(self.kwargs['mes'],
                                             self.kwargs['ano'])


class DiasFolga(generics.ListAPIView):
    serializer_class = PeriodoSerializer

    def get_queryset(self):
        return Periodo.objects.periodoFolga(self.kwargs['mes'], self.kwargs['ano'])