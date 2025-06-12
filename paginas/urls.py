from django.urls import path
from .views import PaginaInicial, SobreView, CadastrosView

urlpatterns = [
    path("", PaginaInicial.as_view(), name='index'),
	path("sobre/", SobreView.as_view(), name='sobre'),
	path("cadastros/", CadastrosView.as_view(), name='listar-cadastros'),
]
