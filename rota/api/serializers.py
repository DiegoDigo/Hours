from rest_framework import serializers
from linha.models import Linha, Carro


class LinhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linha
        fields = '__all__'


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'