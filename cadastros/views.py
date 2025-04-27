from django.shortcuts import render
from .models import Grupo, Turma, Funcao, Disponibilidade, Situacao, Membro, AtualizacaoMembro, IndiceComprometimento, Pastoral
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

# CreateView
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

class AtualizacaoMembroCreate(CreateView):
	model = AtualizacaoMembro
	fields = ['membro', 'data_atualizacao', 'observacao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova atualização de membros',
	}