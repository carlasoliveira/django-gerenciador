from django.urls import path, include
from .views import GrupoCreate
from django.views.generic import TemplateView


urlpatterns = [
    path('grupo/', GrupoCreate.as_view(), name="cadastrar-grupo"),
]
