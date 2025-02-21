from django.db import models
from .usuario import Usuario
from decimal import Decimal
from datetime import date

class Cliente(Usuario):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    objetivo_principal = models.CharField(max_length=255)
    nivel_atividade_fisica = models.CharField(max_length=50)
    restricoes_alimentares = models.JSONField(default=list)
    meta_peso = models.DecimalField(max_digits=5, decimal_places=2)
    meta_calorias = models.IntegerField()

    def calcular_imc(self):
        """Calcula o IMC do cliente"""
        if self.altura and self.peso:
            altura_metros = Decimal(str(self.altura))
            return self.peso / (altura_metros * altura_metros)
        return None

    def registrar_refeicao_consumida(self, refeicao):
        """Registra uma refeição consumida pelo cliente"""
        from .relatorio_consumo import RelatorioConsumo
        relatorio = RelatorioConsumo.objects.create(
            cliente=self,
            data=date.today(),
            calorias_totais=refeicao.calorias,
            meta_calorica=self.meta_calorias
        )
        return relatorio

    def registrar_treino_realizado(self, treino):
        """Registra um treino realizado pelo cliente"""
        from .relatorio_treinos import RelatorioTreinos
        relatorio = RelatorioTreinos.objects.create(
            cliente=self,
            data=date.today(),
            treino=treino
        )
        return relatorio

    def atualizar_progresso(self, peso, imc, observacoes=""):
        """Atualiza o progresso do cliente"""
        from .registro_progresso import RegistroProgresso
        registro = RegistroProgresso.objects.create(
            cliente=self,
            data=date.today(),
            peso=peso,
            imc=imc,
            observacoes=observacoes
        )
        self.peso = peso
        self.save()
        return registro

    class Meta:
        db_table = 'cliente' 