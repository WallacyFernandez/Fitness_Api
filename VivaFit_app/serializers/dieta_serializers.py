from rest_framework import serializers
from ..models import Dieta, Refeicao, Alimento, RefeicaoAlimento

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = ['id', 'nome', 'caloria_por_grama', 'porcao', 
                 'proteinas', 'carboidratos', 'gorduras']

class RefeicaoAlimentoSerializer(serializers.ModelSerializer):
    alimento = AlimentoSerializer(read_only=True)
    
    class Meta:
        model = RefeicaoAlimento
        fields = ['id', 'alimento', 'quantidade']

class RefeicaoSerializer(serializers.ModelSerializer):
    alimentos = RefeicaoAlimentoSerializer(source='refeicaoalimento_set', many=True, read_only=True)
    macronutrientes = serializers.SerializerMethodField()

    class Meta:
        model = Refeicao
        fields = ['id', 'tipo', 'horario', 'calorias', 'alimentos', 'macronutrientes']

    def get_macronutrientes(self, obj):
        return obj.calcular_macronutrientes()

class DietaSerializer(serializers.ModelSerializer):
    refeicoes = RefeicaoSerializer(many=True, read_only=True)
    progresso = serializers.SerializerMethodField()
    calorias_totais = serializers.SerializerMethodField()
    relatorio = serializers.SerializerMethodField()

    class Meta:
        model = Dieta
        fields = ['id', 'cliente', 'nutricionista', 'data_inicio', 'data_fim',
                 'meta_calorica_diaria', 'refeicoes', 'progresso',
                 'calorias_totais', 'relatorio']

    def get_progresso(self, obj):
        return obj.verificar_progresso()

    def get_calorias_totais(self, obj):
        return obj.calcular_calorias_totais()

    def get_relatorio(self, obj):
        return obj.gerar_relatorio() 