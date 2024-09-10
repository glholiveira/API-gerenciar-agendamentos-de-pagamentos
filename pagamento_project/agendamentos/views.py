from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Agendamento
from .serializers import AgendamentoSerializer

@api_view(['GET', 'POST'])
def agendamentos(request):
    if request.method == 'GET':
        # Listar todos os agendamentos
        agendamentos = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Criar um novo agendamento
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def agendamento_detail(request, id):
    try:
        agendamento = Agendamento.objects.get(id=id)
    except Agendamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Consultar agendamento pelo id
        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # Deletar agendamento pelo id
        agendamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
