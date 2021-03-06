from rest_framework import serializers

from core.models import Salas
from core.models import Agendamentos
from core.models import Logs

class SalasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salas
        depth = 1
        fields = [
            'numero',
            'capacidade',
            'obs'
        ]

class AgendamentosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamentos
        depth = 1
        fields = [
            'id',
            'titulo',
            'sala',
            'data',
            'inicio',
            'termino'
        ]

class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        depth = 1
        fields = [
            'log',
            'service',
            'data',
            'sala'
        ]
