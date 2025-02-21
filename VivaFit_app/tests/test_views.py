from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from VivaFit_app.models import (
    Cliente, Nutricionista, Dieta, RelatorioConsumo, 
    Refeicao, Personal, Treino, RelatorioTreinos, RotinaTreino
)
from datetime import date

class ClienteViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.cliente = Cliente.objects.create(
            username='cliente_test',
            email='cliente@test.com',
            password='senha123',
            nome='Cliente Teste',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=70.5,
            altura=1.75,
            meta_peso=65.0,
            meta_calorias=2000,
            objetivo_principal='Emagrecer',
            nivel_atividade_fisica='Moderado'
        )
        self.client.force_authenticate(user=self.cliente)

    def test_list_clientes(self):
        url = reverse('cliente-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_cliente(self):
        url = reverse('cliente-list')
        data = {
            'username': 'novo_cliente',
            'email': 'novo@test.com',
            'password': 'senha123',
            'nome': 'Novo Cliente',
            'data_nascimento': '1995-01-01',
            'telefone': '987654321',
            'peso': 65.0,
            'altura': 1.70,
            'meta_peso': 60.0,
            'meta_calorias': 1800,
            'objetivo_principal': 'Emagrecer',
            'nivel_atividade_fisica': 'Moderado'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DietaViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.nutricionista = Nutricionista.objects.create(
            username='nutri_test',
            email='nutri@test.com',
            password='senha123',
            nome='Nutricionista Teste',
            data_nascimento=date(1985, 1, 1),
            telefone='987654321',
            crn='12345',
            especialidade='Esportiva'
        )
        self.cliente = Cliente.objects.create(
            username='cliente_test',
            email='cliente@test.com',
            password='senha123',
            nome='Cliente Teste',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=70.5,
            altura=1.75,
            meta_peso=65.0,
            meta_calorias=2000,
            objetivo_principal='Emagrecer',
            nivel_atividade_fisica='Moderado'
        )
        self.nutricionista.clientes.add(self.cliente)
        self.client.force_authenticate(user=self.nutricionista)

    def test_create_dieta(self):
        url = reverse('dieta-list')
        data = {
            'cliente': self.cliente.id,
            'nutricionista': self.nutricionista.id,
            'data_inicio': '2024-01-01',
            'data_fim': '2024-02-01',
            'meta_calorica_diaria': 2000
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_dietas(self):
        dieta = Dieta.objects.create(
            cliente=self.cliente,
            nutricionista=self.nutricionista,
            data_inicio=date(2024, 1, 1),
            data_fim=date(2024, 2, 1),
            meta_calorica_diaria=2000
        )
        url = reverse('dieta-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class RelatorioConsumoViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.nutricionista = Nutricionista.objects.create(
            username='nutri_test',
            email='nutri@test.com',
            password='senha123',
            nome='Nutricionista Teste',
            data_nascimento=date(1985, 1, 1),
            telefone='987654321',
            crn='12345',
            especialidade='Esportiva'
        )
        self.cliente = Cliente.objects.create(
            username='cliente_test',
            email='cliente@test.com',
            password='senha123',
            nome='Cliente Teste',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=70.5,
            altura=1.75,
            meta_peso=65.0,
            meta_calorias=2000,
            objetivo_principal='Emagrecer',
            nivel_atividade_fisica='Moderado'
        )
        self.relatorio = RelatorioConsumo.objects.create(
            cliente=self.cliente,
            nutricionista=self.nutricionista,
            data=date.today(),
            calorias_totais=1800,
            meta_calorica=2000
        )
        self.client.force_authenticate(user=self.cliente)

    def test_adicionar_refeicao(self):
        dieta = Dieta.objects.create(
            cliente=self.cliente,
            nutricionista=self.nutricionista,
            data_inicio=date(2024, 1, 1),
            data_fim=date(2024, 2, 1),
            meta_calorica_diaria=2000
        )
        
        refeicao = Refeicao.objects.create(
            dieta=dieta,
            tipo='ALMOCO',
            horario='12:00',
            calorias=500
        )
        url = reverse('relatorioconsumo-adicionar-refeicao', args=[self.relatorio.id])
        data = {'refeicao_id': refeicao.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_calcular_progresso(self):
        url = reverse('relatorioconsumo-calcular-progresso', args=[self.relatorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('progresso', response.data)

class RelatorioTreinosViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.personal = Personal.objects.create(
            username='personal2',
            email='personal2@test.com',
            nome='Personal Teste 2',
            data_nascimento=date(1988, 1, 1),
            telefone='999999999',
            cref='54321',
            especialidade='Musculação'
        )
        self.cliente = Cliente.objects.create(
            username='cliente_test',
            email='cliente@test.com',
            password='senha123',
            nome='Cliente Teste',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=70.5,
            altura=1.75,
            meta_peso=65.0,
            meta_calorias=2000,
            objetivo_principal='Emagrecer',
            nivel_atividade_fisica='Moderado'
        )
        self.relatorio = RelatorioTreinos.objects.create(
            cliente=self.cliente,
            personal=self.personal,
            data=date.today()
        )
        self.client.force_authenticate(user=self.cliente)

        self.rotina = RotinaTreino.objects.create(
            cliente=self.cliente,
            data_inicio=date(2024, 1, 1),
            data_fim=date(2024, 3, 1),
            objetivo='Ganho de massa muscular'
        )

    def test_registrar_treino(self):
        url = reverse('relatoriotreinos-registrar-treino', args=[self.relatorio.id])
        treino = Treino.objects.create(
            rotina_treino=self.rotina,
            dia_semana='SEGUNDA',
            tipo_treino='Musculação',
            duracao=60,
            calorias_estimadas=300
        )
        data = {'treino_id': treino.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_calcular_frequencia(self):
        url = reverse('relatoriotreinos-calcular-frequencia', args=[self.relatorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('frequencia', response.data) 