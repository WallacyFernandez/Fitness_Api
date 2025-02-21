from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import RelatorioConsumo, RelatorioTreinos, RegistroProgresso, Treino, Refeicao
from ..serializers import (
    RelatorioConsumoSerializer, 
    RelatorioTreinosSerializer, 
    RegistroProgressoSerializer
)
from rest_framework.permissions import BasePermission

class IsNutricionistaOrClienteOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.nutricionista or request.user == obj.cliente

class IsPersonalOrClienteOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.personal or request.user == obj.cliente

class RelatorioConsumoViewSet(viewsets.ModelViewSet):
    serializer_class = RelatorioConsumoSerializer

    def get_queryset(self):
        return RelatorioConsumo.objects.all()

    @action(detail=True, methods=['post'])
    def adicionar_refeicao(self, request, pk=None):
        relatorio = self.get_object()
        refeicao_id = request.data.get('refeicao_id')
        try:
            refeicao = Refeicao.objects.get(id=refeicao_id)
            relatorio.adicionar_refeicao(refeicao)
            return Response({'message': 'Refeição adicionada com sucesso'})
        except Refeicao.DoesNotExist:
            return Response(
                {'error': 'Refeição não encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['get'])
    def calcular_progresso(self, request, pk=None):
        relatorio = self.get_object()
        return Response({
            'progresso': f"{relatorio.calcular_progresso():.2f}%"
        })

    @action(detail=True, methods=['get'])
    def gerar_resumo(self, request, pk=None):
        relatorio = self.get_object()
        return Response(relatorio.gerar_resumo())

class RelatorioTreinosViewSet(viewsets.ModelViewSet):
    serializer_class = RelatorioTreinosSerializer

    def get_queryset(self):
        return RelatorioTreinos.objects.all()

    @action(detail=True, methods=['post'])
    def registrar_treino(self, request, pk=None):
        relatorio = self.get_object()
        treino_id = request.data.get('treino_id')
        try:
            treino = Treino.objects.get(id=treino_id)
            relatorio.registrar_treino(treino)
            return Response({'message': 'Treino registrado com sucesso'})
        except Treino.DoesNotExist:
            return Response(
                {'error': 'Treino não encontrado'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['get'])
    def gerar_resumo(self, request, pk=None):
        relatorio = self.get_object()
        return Response(relatorio.gerar_resumo())

    @action(detail=True, methods=['get'])
    def calcular_frequencia(self, request, pk=None):
        relatorio = self.get_object()
        return Response({
            'frequencia': f"{relatorio.calcular_frequencia():.2f}%"
        })

class RegistroProgressoViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroProgressoSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return RegistroProgresso.objects.all()
        return RegistroProgresso.objects.filter(cliente=self.request.user) 