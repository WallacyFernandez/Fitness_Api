from rest_framework import viewsets, permissions
from ..models import RotinaTreino, Treino, Exercicio
from ..serializers import (
    RotinaTreinoSerializer, 
    TreinoSerializer, 
    ExercicioSerializer
)

class RotinaTreinoViewSet(viewsets.ModelViewSet):
    serializer_class = RotinaTreinoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'personal'):
            return RotinaTreino.objects.filter(cliente__in=self.request.user.clientes.all())
        return RotinaTreino.objects.filter(cliente=self.request.user)

class TreinoViewSet(viewsets.ModelViewSet):
    serializer_class = TreinoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Treino.objects.filter(rotina_treino__cliente=self.request.user)

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [permissions.IsAuthenticated] 