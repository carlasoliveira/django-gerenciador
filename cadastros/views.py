from django.shortcuts import render
from .models import Grupo, Turma, Funcao, Disponibilidade, Situacao, Membro, Atualizacao, AtualizacaoMembro, IndiceComprometimento
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
class GrupoCreate(CreateView):
    model = Grupo
    fields = ['nome', 'padroeiro']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')



