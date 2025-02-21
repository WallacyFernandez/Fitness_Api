from django.db import models
from .choices import DiaSemana

class Treino(models.Model):
    rotina_treino = models.ForeignKey('RotinaTreino', on_delete=models.CASCADE, related_name='treinos')
    dia_semana = models.CharField(max_length=20, choices=DiaSemana.choices)
    tipo_treino = models.CharField(max_length=100)
    duracao = models.IntegerField()
    calorias_estimadas = models.IntegerField()

    def adicionar_exercicio(self, exercicio):
        """Adiciona um exercício ao treino"""
        exercicio.treino = self
        exercicio.save()
        return exercicio

    def calcular_calorias_estimadas(self):
        """Calcula as calorias estimadas do treino"""
        # Implementação básica - pode ser ajustada conforme necessário
        CALORIAS_POR_MINUTO = 5  # Valor exemplo
        return self.duracao * CALORIAS_POR_MINUTO

    class Meta:
        db_table = 'treino' 