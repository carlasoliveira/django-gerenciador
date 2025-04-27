from django.urls import path, include
from .views import GrupoCreate, TurmaCreate, FuncaoCreate, DisponibilidadeCreate, SituacaoCreate, IndiceComprometimentoCreate, PastoralCreate, MembroCreate, AtualizacaoMembroCreate
from django.views.generic import TemplateView


urlpatterns = [
    path('grupo/', GrupoCreate.as_view(), name="cadastrar-grupo"),
	path('turma/', TurmaCreate.as_view(), name="cadastrar-turma"),
	path('funcao/', FuncaoCreate.as_view(), name="cadastrar-funcao"),
	path('disponibilidade/', DisponibilidadeCreate.as_view(), name="cadastrar-disponibilidade"),
	path('situacao/', SituacaoCreate.as_view(), name="cadastrar-situacao"),
	path('indice-comprometimento/', IndiceComprometimentoCreate.as_view(), name="cadastrar-indice-comprometimento"),
	path('pastoral/', PastoralCreate.as_view(), name="cadastrar-pastoral"),
	path('membro/', MembroCreate.as_view(), name="cadastrar-membro"),
	path('atualizacao/', AtualizacaoMembroCreate.as_view(), name="cadastrar-atualizacao"),
]
