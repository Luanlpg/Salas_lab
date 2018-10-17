from rest_framework import serializers

from .models import Salas
from .models import Agendamentos
from .models import Logs

class SalasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salas
        depth = 1
        fields = [
            'numero',
            'capacidade',
            'status',
            'obs'
        ]

class AgendamentosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamentos
        depth = 1
        fields = [
            'titulo',
            'sala',
            'data',
            'inicio',
            'termino'
        ]
