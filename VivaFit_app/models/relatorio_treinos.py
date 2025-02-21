from django.db import models
from datetime import timedelta, date
from django.core.exceptions import ValidationError

class RelatorioTreinos(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='relatorios_treinos')
    personal = models.ForeignKey('Personal', on_delete=models.CASCADE, related_name='relatorios_treinos')
    data = models.DateField()
    observacoes = models.TextField(null=True, blank=True)
    treinos_realizados = models.ManyToManyField('Treino', related_name='relatorios')

    def registrar_treino(self, treino):
        """Registra um treino realizado"""
        self.treinos_realizados.add(treino)
        self.save()

    def calcular_frequencia(self):
        """Calcula a frequência de treinos nos últimos 30 dias"""
        from django.utils import timezone
        data_inicial = self.data - timedelta(days=30)
        total_treinos = RelatorioTreinos.objects.filter(
            cliente=self.cliente,
            data__gte=data_inicial,
            data__lte=self.data
        ).count()
        return (total_treinos / 30) * 100

    def gerar_resumo(self):
        """Gera um resumo do relatório de treinos"""
        return {
            'data': self.data,
            'treinos_realizados': list(self.treinos_realizados.all().values('tipo_treino', 'duracao')),
            'frequencia': f"{self.calcular_frequencia():.2f}%",
            'observacoes': self.observacoes
        }

    def clean(self):
        """Validação dos dados do relatório de treinos"""
        if self.data > date.today():
            raise ValidationError('Data do relatório não pode ser futura')

    class Meta:
        db_table = 'relatorio_treinos' 