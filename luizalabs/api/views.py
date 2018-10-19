from django.shortcuts import render
from django.http import Http404

from .serializer import SalasSerializer
from .serializer import AgendamentosSerializer
from .serializer import LogsSerializer

from core.models import Salas
from core.models import Agendamentos
from core.models import Logs

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

class SalasListView(APIView):
    """
    View que lista e cadastra salas.
    """
    serializer_class = SalasSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Salas.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Logs.objects.create(
                sala=int(request.data['numero']),
                log='Criação de sala.',
                service='CADASTRO'
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalasDetailView(APIView):
    """
    View que mostra, altera e apaga salas.
    """
    serializer_class = SalasSerializer

    def get_sala(self, pk):
        try:
            return Salas.objects.get(pk=pk)
        except Salas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sala = self.get_sala(pk)
        serializer = self.serializer_class(sala)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sala = self.get_sala(pk)
        serializer = self.serializer_class(sala, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Logs.objects.create(
                sala=int(request.data['numero']),
                log='Edição de sala.',
                service='EDIÇÃO'
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sala = self.get_sala(pk)
        sala.delete()
        Logs.objects.create(
            sala=int(request.data['numero']),
            log='Remoção de sala.',
            service='REMOÇÃO'
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgendarView(APIView):
    """
    View que agenda horário.
    """
    serializer_class = AgendamentosSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Logs.objects.create(
                sala=int(request.data['sala']),
                log='Criação de Agendamento.',
                service='AGENDAMENTO'
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgendamentosListView(APIView):
    """
    View que lista agendamentos.
    """
    serializer_class = AgendamentosSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Agendamentos.objects.all(), many=True)
        return Response(serializer.data)


class AgendamentosDetailView(APIView):
    """
    View que lista agendamentos especificos, e permite alteraçẽs
    e edições no mesmo.
    """
    serializer_class = AgendamentosSerializer

    def get_agendamento(self, pk):
        try:
            return Agendamentos.objects.get(id=pk)
        except Agendamentos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        agendamento = self.get_agendamento(pk)
        serializer = self.serializer_class(agendamento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        agendamento = self.get_agendamento(pk)
        serializer = self.serializer_class(agendamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Logs.objects.create(
                sala=int(request.data['sala']),
                log='Edição de agendamento.',
                service='EDIÇÃO'
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        agendamento = self.get_agendamento(pk)
        agendamento.delete()
        Logs.objects.create(
            sala=int(request.data['sala']),
            log='Remoção de agendamento.',
            service='CANCELAMENTO'
        )
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogsListView(APIView):
    """
    View que mostra logs do sistema.
    """
    serializer_class = LogsSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Logs.objects.all(), many=True)
        return Response(serializer.data)
