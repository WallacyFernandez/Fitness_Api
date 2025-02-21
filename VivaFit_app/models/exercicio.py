from django.db import models

class Exercicio(models.Model):
    treino = models.ForeignKey('Treino', on_delete=models.CASCADE, related_name='exercicios')
    nome = models.CharField(max_length=255)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    carga = models.DecimalField(max_digits=5, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'exercicio' 