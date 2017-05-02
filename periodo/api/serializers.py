from rest_framework import serializers
from periodo.models import Periodo
from rota.api.serializers import LinhaSerializer, CarroSerializer


class PeriodoSerializer(serializers.ModelSerializer):
    linha = LinhaSerializer(read_only=True)
    carro = CarroSerializer(read_only=True)

    class Meta:
        model = Periodo
        fields = '__all__'


class CreatePeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'