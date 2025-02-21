from rest_framework import viewsets, permissions
from ..models import Cliente, Nutricionista, Personal
from ..serializers import (
    ClienteSerializer, 
    NutricionistaSerializer, 
    PersonalSerializer
)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Cliente.objects.all()
        return Cliente.objects.filter(id=self.request.user.id)

class NutricionistaViewSet(viewsets.ModelViewSet):
    queryset = Nutricionista.objects.all()
    serializer_class = NutricionistaSerializer

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer 