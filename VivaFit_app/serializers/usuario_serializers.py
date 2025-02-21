from rest_framework import serializers
from ..models import Cliente, Nutricionista, Personal

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'data_nascimento', 
                 'peso', 'altura', 'objetivo_principal', 'nivel_atividade_fisica',
                 'restricoes_alimentares', 'meta_peso', 'meta_calorias']
        extra_kwargs = {'senha': {'write_only': True}}

class NutricionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricionista
        fields = ['id', 'nome', 'email', 'telefone', 'data_nascimento',
                 'crn', 'especialidade']
        extra_kwargs = {'senha': {'write_only': True}}

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ['id', 'nome', 'email', 'telefone', 'data_nascimento',
                 'cref', 'especialidade']
        extra_kwargs = {'senha': {'write_only': True}} 