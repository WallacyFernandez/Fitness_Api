from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, NutricionistaViewSet, PersonalViewSet,
    DietaViewSet, RefeicaoViewSet, AlimentoViewSet,
    RotinaTreinoViewSet, TreinoViewSet, ExercicioViewSet,
    RelatorioConsumoViewSet, RelatorioTreinosViewSet, RegistroProgressoViewSet
)

router = DefaultRouter()

# Rotas de Usuários
router.register(r'clientes', ClienteViewSet)
router.register(r'nutricionistas', NutricionistaViewSet)
router.register(r'personais', PersonalViewSet)

# Rotas de Dieta
router.register(r'dietas', DietaViewSet, basename='dieta')
router.register(r'refeicoes', RefeicaoViewSet, basename='refeicao')
router.register(r'alimentos', AlimentoViewSet)

# Rotas de Treino
router.register(r'rotinas-treino', RotinaTreinoViewSet, basename='rotina-treino')
router.register(r'treinos', TreinoViewSet, basename='treino')
router.register(r'exercicios', ExercicioViewSet)

# Rotas de Relatórios
router.register(r'relatorios-consumo', RelatorioConsumoViewSet, basename='relatorioconsumo')
router.register(r'relatorios-treinos', RelatorioTreinosViewSet, basename='relatoriotreinos')
router.register(r'registros-progresso', RegistroProgressoViewSet, basename='registro-progresso')

urlpatterns = [
    path('', include(router.urls)),
] 