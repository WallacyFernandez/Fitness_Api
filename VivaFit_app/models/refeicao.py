from django.db import models
from .choices import TipoRefeicao

class Refeicao(models.Model):
    dieta = models.ForeignKey('Dieta', on_delete=models.CASCADE, related_name='refeicoes_relacionadas')
    tipo = models.CharField(max_length=50, choices=TipoRefeicao.choices)
    horario = models.TimeField()
    calorias = models.IntegerField()
    alimentos = models.ManyToManyField('Alimento', through='RefeicaoAlimento', related_name='refeicoes')

    def adicionar_alimento(self, alimento, quantidade):
        """Adiciona um alimento à refeição com sua quantidade"""
        RefeicaoAlimento.objects.create(
            refeicao=self,
            alimento=alimento,
            quantidade=quantidade
        )
        self.calorias += (alimento.caloria_por_grama * quantidade)
        self.save()

    def remover_alimento(self, alimento):
        """Remove um alimento da refeição"""
        refeicao_alimento = RefeicaoAlimento.objects.get(
            refeicao=self,
            alimento=alimento
        )
        self.calorias -= (alimento.caloria_por_grama * refeicao_alimento.quantidade)
        refeicao_alimento.delete()
        self.save()

    def calcular_macronutrientes(self):
        """Calcula os macronutrientes totais da refeição"""
        refeicao_alimentos = RefeicaoAlimento.objects.filter(refeicao=self)
        macros = {
            'proteinas': 0,
            'carboidratos': 0,
            'gorduras': 0
        }
        
        for ra in refeicao_alimentos:
            macros['proteinas'] += ra.alimento.proteinas * ra.quantidade
            macros['carboidratos'] += ra.alimento.carboidratos * ra.quantidade
            macros['gorduras'] += ra.alimento.gorduras * ra.quantidade
        
        return macros

    class Meta:
        db_table = 'refeicao'

class RefeicaoAlimento(models.Model):
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    alimento = models.ForeignKey('Alimento', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=6, decimal_places=2)  # em gramas

    class Meta:
        db_table = 'refeicao_alimento' 