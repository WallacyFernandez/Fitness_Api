from rest_framework import viewsets, permissions
from ..models import Dieta, Refeicao, Alimento, Cliente, Nutricionista, RefeicaoAlimento
from ..serializers import (
    DietaSerializer, 
    RefeicaoSerializer, 
    AlimentoSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class DietaViewSet(viewsets.ModelViewSet):
    serializer_class = DietaSerializer

    def get_queryset(self):
        return Dieta.objects.all()

    @action(detail=True, methods=['post'])
    def adicionar_refeicao(self, request, pk=None):
        dieta = self.get_object()
        refeicao_id = request.data.get('refeicao_id')
        try:
            refeicao = Refeicao.objects.get(id=refeicao_id)
            dieta.adicionar_refeicao(refeicao)
            return Response({'message': 'Refeição adicionada com sucesso'})
        except Refeicao.DoesNotExist:
            return Response(
                {'error': 'Refeição não encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['get'])
    def verificar_progresso(self, request, pk=None):
        dieta = self.get_object()
        return Response(dieta.verificar_progresso())

    @action(detail=True, methods=['get'])
    def gerar_relatorio(self, request, pk=None):
        dieta = self.get_object()
        return Response(dieta.gerar_relatorio())

class RefeicaoViewSet(viewsets.ModelViewSet):
    serializer_class = RefeicaoSerializer

    def get_queryset(self):
        return Refeicao.objects.all()

    @action(detail=True, methods=['post'])
    def adicionar_alimento(self, request, pk=None):
        refeicao = self.get_object()
        alimento_id = request.data.get('alimento_id')
        quantidade = request.data.get('quantidade')

        try:
            alimento = Alimento.objects.get(id=alimento_id)
            refeicao.adicionar_alimento(alimento, quantidade)
            return Response({'message': 'Alimento adicionado com sucesso'})
        except Alimento.DoesNotExist:
            return Response(
                {'error': 'Alimento não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['post'])
    def remover_alimento(self, request, pk=None):
        refeicao = self.get_object()
        alimento_id = request.data.get('alimento_id')

        try:
            alimento = Alimento.objects.get(id=alimento_id)
            refeicao.remover_alimento(alimento)
            return Response({'message': 'Alimento removido com sucesso'})
        except (Alimento.DoesNotExist, RefeicaoAlimento.DoesNotExist):
            return Response(
                {'error': 'Alimento não encontrado na refeição'},
                status=status.HTTP_404_NOT_FOUND
            )

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

    @action(detail=True, methods=['post'])
    def adicionar_alimento(self, request, pk=None):
        alimento = self.get_object()
        refeicao_id = request.data.get('refeicao_id')
        quantidade = request.data.get('quantidade')

        try:
            refeicao = Refeicao.objects.get(id=refeicao_id)
            refeicao.adicionar_alimento(alimento, quantidade)
            return Response({'message': 'Alimento adicionado com sucesso'})
        except Refeicao.DoesNotExist:
            return Response(
                {'error': 'Refeição não encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['post'])
    def remover_alimento(self, request, pk=None):
        alimento = self.get_object()
        refeicao_id = request.data.get('refeicao_id')

        try:
            refeicao = Refeicao.objects.get(id=refeicao_id)
            refeicao.remover_alimento(alimento)
            return Response({'message': 'Alimento removido com sucesso'})
        except Refeicao.DoesNotExist:
            return Response(
                {'error': 'Refeição não encontrada'},
                status=status.HTTP_404_NOT_FOUND
            ) 