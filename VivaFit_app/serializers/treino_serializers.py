from rest_framework import serializers
from ..models import RotinaTreino, Treino, Exercicio

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'nome', 'series', 'repeticoes', 
                 'carga', 'observacoes']

class TreinoSerializer(serializers.ModelSerializer):
    exercicios = ExercicioSerializer(many=True, read_only=True)
    calorias_estimadas = serializers.SerializerMethodField()

    class Meta:
        model = Treino
        fields = ['id', 'dia_semana', 'tipo_treino', 'duracao',
                 'calorias_estimadas', 'exercicios']

    def get_calorias_estimadas(self, obj):
        return obj.calcular_calorias_estimadas()

class RotinaTreinoSerializer(serializers.ModelSerializer):
    treinos = TreinoSerializer(many=True, read_only=True)

    class Meta:
        model = RotinaTreino
        fields = ['id', 'cliente', 'data_inicio', 'data_fim',
                 'objetivo', 'treinos'] 