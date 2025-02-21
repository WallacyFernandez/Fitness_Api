from django.db import models

class RotinaTreino(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='rotinas_treino')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    objetivo = models.CharField(max_length=255)

    class Meta:
        db_table = 'rotina_treino' 