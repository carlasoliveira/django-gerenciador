from django.shortcuts import render
from django.contrib.auth.models import User
import re
from .models import Grupo, Turma, Funcao, Disponibilidade, Situacao, Membro, AtualizacaoMembro, IndiceComprometimento, Pastoral
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

##### CreateView

class GrupoCreate(CreateView):
    model = Grupo
    fields = ['nome', 'padroeiro']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
		'title': 'Cadastrar novo grupo',
	}
    
class TurmaCreate(CreateView):
	model = Turma
	fields = ['grupo', 'num_turma', 'data_investidura']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova turma',
	}
      
class FuncaoCreate(CreateView):
	model = Funcao
	fields = ['funcao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova função',
	}

class DisponibilidadeCreate(CreateView):
	model = Disponibilidade
	fields = ['dia_semana']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova disponibilidade',
	}

class SituacaoCreate(CreateView):
	model = Situacao
	fields = ['situacao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova situação',
	}

class IndiceComprometimentoCreate(CreateView):
	model = IndiceComprometimento
	fields = ['indice', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar novo índice de comprometimento',
	}

class PastoralCreate(CreateView):
	model = Pastoral
	fields = ['nome', 'sigla']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova pastoral',
	}

class MembroCreate(CreateView):
	model = Membro
	fields = ['nome',
			'data_nascimento', 
			'telefone', 
			'endereco', 
			'nome_pai', 
			'nome_mae', 
			'sacramentos',
			'atuacao_pastorais',
			'grupo',
			'turma', 
			'funcao', 
			'disponibilidade', 
			'situacao', 
			'indice_comprometimento',
			'resumo',
			'observacao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar novo membro',
	}

	def form_valid(self, form):
		telefone = form.instance.telefone
		telefone = re.sub(r'\D', '', telefone)
		usuario = User.objects.update_or_create(username=telefone, defaults={'password': telefone})
		form.instance.usuario = usuario
		url = super().form_valid(form)

		return url

class AtualizacaoMembroCreate(CreateView):
	model = AtualizacaoMembro
	fields = ['membro', 'data_atualizacao', 'observacao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova atualização de membros',
	}

##### UpdateView

class GrupoUpdate(UpdateView):
	model = Grupo
	fields = ['nome', 'padroeiro']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar grupos',
	}

class TurmaUpdate(UpdateView):
	model = Turma
	fields = ['grupo', 'num_turma', 'data_investidura']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar turmas',
	}
	
class FuncaoUpdate(UpdateView):
	model = Funcao
	fields = ['funcao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar funções',
	}

class DisponibilidadeUpdate(UpdateView):
	model = Disponibilidade
	fields = ['dia_semana']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar disponibilidades',
	}

class SituacaoUpdate(UpdateView):
	model = Situacao
	fields = ['situacao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar situações',
	}

class IndiceComprometimentoUpdate(UpdateView):
	model = IndiceComprometimento
	fields = ['indice', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizat índices de comprometimento',
	}

class PastoralUpdate(UpdateView):
	model = Pastoral
	fields = ['nome', 'sigla']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova pastoral',
	}

#### DeleteView

class GrupoDelete(DeleteView):
	model = Grupo
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir grupo',
	}

class TurmaDelete(DeleteView):
	model = Turma
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir turma',
	}

class FuncaoDelete(DeleteView):
	model = Funcao
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir função',
	}

class DisponibilidadeDelete(DeleteView):
	model = Disponibilidade
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir disponibilidade',
	}

class SituacaoDelete(DeleteView):
	model = Situacao
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir situação',
	}

class IndiceComprometimentoDelete(DeleteView):
	model = IndiceComprometimento
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir índice de comprometimento',
	}

class PastoralDelete(DeleteView):
	model = Pastoral
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir pastoral',
	}

#### ListView

class GrupoList(ListView):
	model = Grupo
	template_name = 'listas/campus.html'

