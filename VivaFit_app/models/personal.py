from django.db import models
from .usuario import Usuario

class Personal(Usuario):
    cref = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    clientes = models.ManyToManyField('Cliente', related_name='personais')

    class Meta:
        db_table = 'personal' 