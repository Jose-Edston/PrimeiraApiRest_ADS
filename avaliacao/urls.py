# from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('alunos/', AlunoAPIView.as_view(), name='alunos'),
#     path('alunos/<int:pk>/', AlunoSelecionado.as_view(), name='aluno'),
#     path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes')
# ]

routers = SimpleRouter()
routers.register('alunos', AlunosViewset)
routers.register('avaliacoes', AvaliacaoViewSet)