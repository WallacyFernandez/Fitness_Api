from django.test import TestCase
from VivaFit_app.models import (
    Cliente, Nutricionista, Personal,
    Dieta, Refeicao, Alimento,
    RotinaTreino, Treino, Exercicio
)
from datetime import date, time

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            username='cliente1',
            email='cliente@test.com',
            nome='Cliente Teste',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=70.5,
            altura=1.75,
            objetivo_principal='Emagrecer',
            nivel_atividade_fisica='Moderado',
            restricoes_alimentares='Nenhuma',
            meta_peso=65.0,
            meta_calorias=2000
        )
        
        self.nutricionista = Nutricionista.objects.create(
            username='nutri1',
            email='nutri@test.com',
            nome='Nutricionista Teste',
            data_nascimento=date(1985, 1, 1),
            telefone='987654321',
            crn='12345',
            especialidade='Esportiva'
        )

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nome, 'Cliente Teste')
        self.assertEqual(self.cliente.meta_calorias, 2000)
        self.assertEqual(self.cliente.restricoes_alimentares, 'Nenhuma')

    def test_nutricionista_creation(self):
        self.assertEqual(self.nutricionista.crn, '12345')
        self.assertEqual(self.nutricionista.especialidade, 'Esportiva')

    def test_personal_creation(self):
        personal = Personal.objects.create(
            username='personal1',
            email='personal@test.com',
            nome='Personal Teste',
            data_nascimento=date(1988, 1, 1),
            telefone='999999999',
            cref='54321',
            especialidade='Musculação'
        )
        self.assertEqual(personal.cref, '54321')
        self.assertEqual(personal.especialidade, 'Musculação')

    def test_cliente_restricoes_alimentares(self):
        cliente = Cliente.objects.create(
            username='cliente2',
            email='cliente2@test.com',
            nome='Cliente Teste 2',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=80.0,
            altura=1.80,
            objetivo_principal='Ganho de massa',
            nivel_atividade_fisica='Intenso',
            restricoes_alimentares='Lactose, Glúten',
            meta_peso=85.0,
            meta_calorias=3000
        )
        self.assertEqual(cliente.restricoes_alimentares, 'Lactose, Glúten')

class DietaTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            username='cliente2',
            email='cliente2@test.com',
            nome='Cliente Teste 2',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=70.5,
            altura=1.75,
            objetivo_principal='Emagrecer',
            nivel_atividade_fisica='Moderado',
            meta_peso=65.0,
            meta_calorias=2000
        )

        self.nutricionista = Nutricionista.objects.create(
            username='nutri2',
            email='nutri2@test.com',
            nome='Nutricionista Teste 2',
            data_nascimento=date(1985, 1, 1),
            telefone='987654321',
            crn='12345',
            especialidade='Esportiva'
        )

        self.dieta = Dieta.objects.create(
            cliente=self.cliente,
            nutricionista=self.nutricionista,
            data_inicio=date(2024, 1, 1),
            data_fim=date(2024, 3, 1),
            meta_calorica_diaria=2000
        )

        self.refeicao = Refeicao.objects.create(
            dieta=self.dieta,
            tipo='CAFE_MANHA',
            horario=time(8, 0),
            calorias=500
        )

        self.alimento = Alimento.objects.create(
            nome='Arroz Integral',
            caloria_por_grama=1.3,
            porcao=100.0,
            proteinas=2.6,
            carboidratos=28.2,
            gorduras=0.3
        )

    def test_dieta_creation(self):
        self.assertEqual(self.dieta.meta_calorica_diaria, 2000)
        self.assertEqual(self.dieta.cliente, self.cliente)

    def test_refeicao_creation(self):
        self.assertEqual(self.refeicao.tipo, 'CAFE_MANHA')
        self.assertEqual(self.refeicao.calorias, 500)

    def test_alimento_creation(self):
        self.assertEqual(self.alimento.nome, 'Arroz Integral')
        self.assertEqual(self.alimento.caloria_por_grama, 1.3)

class RotinaTreinoTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            username='cliente3',
            email='cliente3@test.com',
            nome='Cliente Teste 3',
            data_nascimento=date(1990, 1, 1),
            telefone='123456789',
            peso=75.0,
            altura=1.80,
            meta_peso=70.0,
            meta_calorias=2500,
            objetivo_principal='Hipertrofia',
            nivel_atividade_fisica='Intenso'
        )
        
        self.rotina = RotinaTreino.objects.create(
            cliente=self.cliente,
            data_inicio=date(2024, 1, 1),
            data_fim=date(2024, 3, 1),
            objetivo='Ganho de massa muscular'
        )

    def test_rotina_treino_creation(self):
        self.assertEqual(self.rotina.objetivo, 'Ganho de massa muscular')
        self.assertEqual(self.rotina.cliente, self.cliente)

    def test_treino_creation(self):
        treino = Treino.objects.create(
            rotina_treino=self.rotina,
            dia_semana='SEGUNDA',
            tipo_treino='Musculação',
            duracao=60,
            calorias_estimadas=300
        )
        self.assertEqual(treino.tipo_treino, 'Musculação')
        self.assertEqual(treino.dia_semana, 'SEGUNDA')

    def test_exercicio_creation(self):
        treino = Treino.objects.create(
            rotina_treino=self.rotina,
            dia_semana='SEGUNDA',
            tipo_treino='Musculação',
            duracao=60,
            calorias_estimadas=300
        )
        exercicio = Exercicio.objects.create(
            treino=treino,
            nome='Supino Reto',
            series=4,
            repeticoes=12,
            carga=60.0,
            observacoes='Manter cotovelos alinhados'
        )
        self.assertEqual(exercicio.nome, 'Supino Reto')
        self.assertEqual(exercicio.series, 4)