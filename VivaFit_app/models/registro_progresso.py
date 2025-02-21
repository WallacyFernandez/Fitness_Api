from django.db import models
from decimal import Decimal

class RegistroProgresso(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='registros_progresso')
    data = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=4, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True)

    def calcular_variacao_peso(self):
        """Calcula a variação de peso em relação ao registro anterior"""
        registro_anterior = RegistroProgresso.objects.filter(
            cliente=self.cliente,
            data__lt=self.data
        ).order_by('-data').first()
        
        if registro_anterior:
            return self.peso - registro_anterior.peso
        return Decimal('0.0')

    def calcular_variacao_imc(self):
        """Calcula a variação do IMC em relação ao registro anterior"""
        registro_anterior = RegistroProgresso.objects.filter(
            cliente=self.cliente,
            data__lt=self.data
        ).order_by('-data').first()
        
        if registro_anterior:
            return self.imc - registro_anterior.imc
        return Decimal('0.0')

    class Meta:
        db_table = 'registro_progresso' 