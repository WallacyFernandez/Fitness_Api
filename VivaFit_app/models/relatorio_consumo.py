from django.db import models
from decimal import Decimal
from django.core.exceptions import ValidationError

class RelatorioConsumo(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='relatorios_consumo')
    nutricionista = models.ForeignKey('Nutricionista', on_delete=models.CASCADE, related_name='relatorios_consumo')
    data = models.DateField()
    calorias_totais = models.IntegerField()
    meta_calorica = models.IntegerField()
    refeicoes_diarias = models.ManyToManyField('Refeicao', related_name='relatorios')

    def calcular_progresso(self):
        """Calcula o progresso em relação à meta calórica"""
        if self.meta_calorica > 0:
            return (self.calorias_totais / self.meta_calorica) * 100
        return 0

    def adicionar_refeicao(self, refeicao):
        """Adiciona uma refeição ao relatório"""
        self.refeicoes_diarias.add(refeicao)
        self.calorias_totais += refeicao.calorias
        self.save()

    def gerar_resumo(self):
        """Gera um resumo do relatório de consumo"""
        progresso = self.calcular_progresso()
        return {
            'data': self.data,
            'calorias_consumidas': self.calorias_totais,
            'meta_calorica': self.meta_calorica,
            'progresso': f"{progresso:.2f}%",
            'refeicoes': list(self.refeicoes_diarias.all().values('tipo', 'calorias'))
        }

    def clean(self):
        """Validação dos dados do relatório de consumo"""
        if self.calorias_totais < 0:
            raise ValidationError('Calorias totais não podem ser negativas')
        if self.meta_calorica <= 0:
            raise ValidationError('Meta calórica deve ser maior que zero')

    class Meta:
        db_table = 'relatorio_consumo' 