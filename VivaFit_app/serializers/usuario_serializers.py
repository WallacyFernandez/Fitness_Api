from rest_framework import serializers
from ..models import Cliente, Nutricionista, Personal

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id', 'password', 'nome', 'email', 
            'telefone', 'data_nascimento', 'peso', 'altura', 
            'objetivo_principal', 'nivel_atividade_fisica',
            'restricoes_alimentares', 'meta_peso', 'meta_calorias'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Usa o email como username
        validated_data['username'] = validated_data.get('email')
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

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