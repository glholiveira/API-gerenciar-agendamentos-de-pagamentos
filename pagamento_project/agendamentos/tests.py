from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Agendamento

class AgendamentoAPITests(APITestCase):

    def setUp(self):
        # Cria um agendamento de exemplo
        self.agendamento = Agendamento.objects.create(
            data_pagamento="2024-01-10",
            permite_recorrencia=True,
            quantidade_recorrencia=1,
            intervalo_recorrencia=30,
            status_recorrencia="ativo",
            agencia=124545434545,
            conta=56555789,
            valor_pagamento=4444.44
        )
        self.list_url = reverse('agendamentos')
        self.detail_url = reverse('agendamento_detail', args=[self.agendamento.id])

    def test_listar_agendamentos(self):
        # Testa o endpoint de listagem
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_consultar_agendamento_por_id(self):
        # Testa o endpoint de consulta por ID
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.agendamento.id)

    def test_criar_agendamento(self):
        # Testa a criação de um agendamento
        data = {
            "data_pagamento": "2024-02-15",
            "permite_recorrencia": False,
            "quantidade_recorrencia": 1,
            "intervalo_recorrencia": 30,
            "status_recorrencia": "inativo",
            "agencia": 123456789,
            "conta": 987654321,
            "valor_pagamento": 1234.56
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_deletar_agendamento(self):
        # Testa a deleção de um agendamento
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Agendamento.objects.filter(id=self.agendamento.id).exists())
