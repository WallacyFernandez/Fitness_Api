from django.db import models
from .usuario import Usuario

class Nutricionista(Usuario):
    crn = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    clientes = models.ManyToManyField('Cliente', related_name='nutricionistas')

    class Meta:
        db_table = 'nutricionista' 