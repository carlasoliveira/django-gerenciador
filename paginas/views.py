from django.shortcuts import render

#Renderiza uma página WEB
from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = "paginas/index.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    
class CadastrosView(TemplateView):
	template_name = "paginas/cadastros.html"