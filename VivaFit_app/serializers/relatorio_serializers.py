from rest_framework import serializers
from ..models import RelatorioConsumo, RelatorioTreinos, RegistroProgresso
from .treino_serializers import TreinoSerializer
from .dieta_serializers import RefeicaoSerializer

class RelatorioConsumoSerializer(serializers.ModelSerializer):
    refeicoes_diarias = RefeicaoSerializer(many=True, read_only=True)
    progresso = serializers.SerializerMethodField()
    resumo = serializers.SerializerMethodField()

    class Meta:
        model = RelatorioConsumo
        fields = ['id', 'cliente', 'nutricionista', 'data',
                 'calorias_totais', 'meta_calorica', 'refeicoes_diarias',
                 'progresso', 'resumo']

    def get_progresso(self, obj):
        return f"{obj.calcular_progresso():.2f}%"

    def get_resumo(self, obj):
        return obj.gerar_resumo()

class RelatorioTreinosSerializer(serializers.ModelSerializer):
    treinos_realizados = TreinoSerializer(many=True, read_only=True)
    frequencia = serializers.SerializerMethodField()
    resumo = serializers.SerializerMethodField()

    class Meta:
        model = RelatorioTreinos
        fields = ['id', 'cliente', 'personal', 'data', 
                 'treinos_realizados', 'observacoes', 
                 'frequencia', 'resumo']

    def get_frequencia(self, obj):
        return f"{obj.calcular_frequencia():.2f}%"

    def get_resumo(self, obj):
        return obj.gerar_resumo()

class RegistroProgressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProgresso
        fields = ['id', 'cliente', 'data', 'peso', 'imc', 'observacoes'] 