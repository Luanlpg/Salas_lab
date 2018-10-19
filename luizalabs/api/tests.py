from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Salas


class SalasTestCase(APITestCase):
    """
    Classe de testes para todos os metodos HTTP utilizados.
    """

    def setUp(self):
        self.client = APIClient()
        teste = Salas.objects.create(
                                        numero=1,
                                        capacidade=40,
                                        obs= 'teste'
                                    )

    def test_get(self):
        response = self.client.get('/api/salas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post('/api/salas/',
            {
                'numero': 2,
                'capacidade': 40,
                'obs': 'S/C'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_error(self):
        # tem que errar, pois já existe!
        response = self.client.post('/api/salas/',
            {
                'numero': 1,
                'capacidade': 40,
                'obs': 'teste'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_error(self):
        response = self.client.put('/api/salas/2/',
            {
                'numero': 1,
                'capacidade': 40,
                'obs': 'testado'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_error(self):
        response = self.client.put('/api/salas/1/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
