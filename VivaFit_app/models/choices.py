from django.db import models

class TipoRefeicao(models.TextChoices):
    CAFE_MANHA = 'CAFE_MANHA', 'Café da Manhã'
    LANCHE_MANHA = 'LANCHE_MANHA', 'Lanche da Manhã'
    ALMOCO = 'ALMOCO', 'Almoço'
    LANCHE_TARDE = 'LANCHE_TARDE', 'Lanche da Tarde'
    JANTAR = 'JANTAR', 'Jantar'
    CEIA = 'CEIA', 'Ceia'

class DiaSemana(models.TextChoices):
    SEGUNDA = 'SEGUNDA', 'Segunda-feira'
    TERCA = 'TERCA', 'Terça-feira'
    QUARTA = 'QUARTA', 'Quarta-feira'
    QUINTA = 'QUINTA', 'Quinta-feira'
    SEXTA = 'SEXTA', 'Sexta-feira'
    SABADO = 'SABADO', 'Sábado'
    DOMINGO = 'DOMINGO', 'Domingo' 