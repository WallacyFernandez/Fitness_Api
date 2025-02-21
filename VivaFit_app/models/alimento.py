from django.db import models

class Alimento(models.Model):
    nome = models.CharField(max_length=255)
    caloria_por_grama = models.DecimalField(max_digits=6, decimal_places=2)
    porcao = models.DecimalField(max_digits=6, decimal_places=2)
    proteinas = models.DecimalField(max_digits=6, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=6, decimal_places=2)
    gorduras = models.DecimalField(max_digits=6, decimal_places=2)
    refeicao = models.ManyToManyField('Refeicao', related_name='alimentos_relacionados')

    class Meta:
        db_table = 'alimento' 