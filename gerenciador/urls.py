from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("paginas.urls")),
	path("cadastro/", include("cadastros.urls")),
	path("", include("usuarios.urls")),
]