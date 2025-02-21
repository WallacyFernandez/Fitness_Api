from django.db import models
from datetime import date

class Dieta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='dietas')
    nutricionista = models.ForeignKey('Nutricionista', on_delete=models.CASCADE, related_name='dietas_prescritas')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    meta_calorica_diaria = models.IntegerField()
    refeicoes = models.ManyToManyField('Refeicao', related_name='dietas_relacionadas')

    def adicionar_refeicao(self, refeicao):
        """Adiciona uma refeição à dieta"""
        self.refeicoes.add(refeicao)
        self.save()
        return refeicao

    def calcular_calorias_totais(self):
        """Calcula o total de calorias da dieta"""
        return sum(refeicao.calorias for refeicao in self.refeicoes.all())

    def verificar_progresso(self):
        """Verifica o progresso da dieta"""
        from .relatorio_consumo import RelatorioConsumo
        
        hoje = date.today()
        if self.data_inicio <= hoje <= self.data_fim:
            relatorios = RelatorioConsumo.objects.filter(
                cliente=self.cliente,
                data__gte=self.data_inicio,
                data__lte=hoje
            )
            
            if not relatorios.exists():
                return {
                    'status': 'Sem registros',
                    'aderencia': 0,
                    'media_calorias': 0
                }
            
            total_calorias = sum(r.calorias_totais for r in relatorios)
            media_calorias = total_calorias / relatorios.count()
            aderencia = (media_calorias / self.meta_calorica_diaria) * 100
            
            return {
                'status': 'Em andamento',
                'aderencia': f"{aderencia:.2f}%",
                'media_calorias': media_calorias
            }
        
        elif hoje < self.data_inicio:
            return {'status': 'Não iniciada'}
        else:
            return {'status': 'Finalizada'}

    def gerar_relatorio(self):
        """Gera um relatório completo da dieta"""
        progresso = self.verificar_progresso()
        return {
            'cliente': self.cliente.nome,
            'nutricionista': self.nutricionista.nome,
            'periodo': {
                'inicio': self.data_inicio,
                'fim': self.data_fim
            },
            'meta_calorica': self.meta_calorica_diaria,
            'calorias_totais': self.calcular_calorias_totais(),
            'refeicoes': list(self.refeicoes.all().values('tipo', 'horario', 'calorias')),
            'progresso': progresso
        }

    class Meta:
        db_table = 'dieta' 