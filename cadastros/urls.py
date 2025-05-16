from django.urls import path, include
from .views import GrupoCreate, TurmaCreate, FuncaoCreate, DisponibilidadeCreate, SituacaoCreate, IndiceComprometimentoCreate, PastoralCreate, MembroCreate, AtualizacaoMembroCreate
from .views import GrupoUpdate, TurmaUpdate, FuncaoUpdate, DisponibilidadeUpdate, SituacaoUpdate, IndiceComprometimentoUpdate, PastoralUpdate
from .views import GrupoDelete, TurmaDelete, FuncaoDelete, DisponibilidadeDelete, SituacaoDelete, IndiceComprometimentoDelete, PastoralDelete
from .views import GrupoList
from django.views.generic import TemplateView


urlpatterns = [
	##### CreateView URLs
    path('grupo/', GrupoCreate.as_view(), name="cadastrar-grupo"),
	path('turma/', TurmaCreate.as_view(), name="cadastrar-turma"),
	path('funcao/', FuncaoCreate.as_view(), name ="cadastrar-funcao"),
	path('disponibilidade/', DisponibilidadeCreate.as_view(), name="cadastrar-disponibilidade"),
	path('situacao/', SituacaoCreate.as_view(), name="cadastrar-situacao"),
	path('indice-comprometimento/', IndiceComprometimentoCreate.as_view(), name="cadastrar-indice-comprometimento"),
	path('pastoral/', PastoralCreate.as_view(), name="cadastrar-pastoral"),
	path('membro/', MembroCreate.as_view(), name="cadastrar-membro"),
	path('atualizacao/', AtualizacaoMembroCreate.as_view(), name="cadastrar-atualizacao"),

	##### UpdateView URLs
	path('editar/grupo/<int:pk>/', GrupoUpdate.as_view(), name="editar-grupo"),
	path('editar/turma/<int:pk>/', TurmaUpdate.as_view(), name="editar-turma"),
	path('editar/funcao/<int:pk>/', FuncaoUpdate.as_view(), name="editar-funcao"),
	path('editar/disponibilidade/<int:pk>/', DisponibilidadeUpdate.as_view(), name="editar-disponibilidade"),
	path('editar/situacao/<int:pk>/', SituacaoUpdate.as_view(), name="editar-situacao"),
	path('editar/indice-comprometimento/<int:pk>/', IndiceComprometimentoUpdate.as_view(), name="editar-indice-comprometimento"),
	path('editar/pastoral/<int:pk>/', PastoralUpdate.as_view(), name="editar-pastoral"),

	##### DeleteView URLs
	path('excluir/grupo/<int:pk>/', GrupoDelete.as_view(), name="deletar-grupo"),
	path('excluir/turma/<int:pk>/', TurmaDelete.as_view(), name="deletar-turma"),
	path('excluir/funcao/<int:pk>/', FuncaoDelete.as_view(), name="deletar-funcao"),
	path('excluir/disponibilidade/<int:pk>/', DisponibilidadeDelete.as_view(), name="deletar-disponibilidade"),
	path('excluir/situacao/<int:pk>/', SituacaoDelete.as_view(), name="deletar-situacao"),
	path('excluir/indice-comprometimento/<int:pk>/', IndiceComprometimentoDelete.as_view(), name="deletar-indice-comprometimento"),
	path('excluir/pastoral/<int:pk>/', PastoralDelete.as_view(), name="deletar-pastoral"),

	##### ListView URLs
	path('listar/grupos/', GrupoList.as_view(), name="listar-grupo"),
]
