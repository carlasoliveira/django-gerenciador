from django.shortcuts import render
from django.contrib.auth.models import User
import re
from .models import Grupo, Turma, Funcao, Disponibilidade, Situacao, Membro, AtualizacaoMembro, IndiceComprometimento, Pastoral
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

##### CreateView

class GrupoCreate(LoginRequiredMixin, CreateView):
    model = Grupo
    fields = ['nome', 'padroeiro']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
		'title': 'Cadastrar novo grupo',
		'name_button': 'Cadastrar grupo',
	}
    
class TurmaCreate(LoginRequiredMixin, CreateView):
	model = Turma
	fields = ['grupo', 'num_turma', 'data_investidura']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova turma',
		'name_button': 'Cadastrar turma',
	}
      
class FuncaoCreate(LoginRequiredMixin, CreateView):
	model = Funcao
	fields = ['funcao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova função',
		'name_button': 'Cadastrar função',
	}

class DisponibilidadeCreate(LoginRequiredMixin, CreateView):
	model = Disponibilidade
	fields = ['dia_semana']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova disponibilidade',
		'name_button': 'Cadastrar disponibilidade',
	}

class SituacaoCreate(LoginRequiredMixin, CreateView):
	model = Situacao
	fields = ['situacao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova situação',
		'name_button': 'Cadastrar situação',
	}

class IndiceComprometimentoCreate(LoginRequiredMixin, CreateView):
	model = IndiceComprometimento
	fields = ['indice', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar novo índice de comprometimento',
		'name_button': 'Cadastrar índice de comprometimento',
	}

class PastoralCreate(LoginRequiredMixin, CreateView):
	model = Pastoral
	fields = ['nome', 'sigla']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova pastoral',
		'name_button': 'Cadastrar pastoral',	
	}

class MembroCreate(LoginRequiredMixin, CreateView):
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
		'name_button': 'Cadastrar membro',
	}

	def form_valid(self, form):
		telefone = form.instance.telefone
		telefone = re.sub(r'\D', '', telefone)
		usuario = User.objects.update_or_create(username=telefone, defaults={'password': telefone})
		form.instance.usuario = usuario
		url = super().form_valid(form)

		return url

class AtualizacaoMembroCreate(LoginRequiredMixin, CreateView):
	model = AtualizacaoMembro
	fields = ['membro', 'data_atualizacao', 'observacao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Cadastrar nova atualização de membros',
		'name_button': 'Cadastrar atualização de membro',
	}

##### UpdateView

class GrupoUpdate(LoginRequiredMixin, UpdateView):
	model = Grupo
	fields = ['nome', 'padroeiro']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar grupos',
		'name_button': 'Atualizar grupo',
	}

class TurmaUpdate(LoginRequiredMixin, UpdateView):
	model = Turma
	fields = ['grupo', 'num_turma', 'data_investidura']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar turmas',
		'name_button': 'Atualizar turma',
	}
	
class FuncaoUpdate(LoginRequiredMixin, UpdateView):
	model = Funcao
	fields = ['funcao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar funções',
		'name_button': 'Atualizar função',
	}

class DisponibilidadeUpdate(LoginRequiredMixin, UpdateView):
	model = Disponibilidade
	fields = ['dia_semana']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar disponibilidades',
		'name_button': 'Atualizar disponibilidade',
	}

class SituacaoUpdate(LoginRequiredMixin, UpdateView):
	model = Situacao
	fields = ['situacao', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar situações',
		'name_button': 'Atualizar situação',
	}

class IndiceComprometimentoUpdate(LoginRequiredMixin, UpdateView):
	model = IndiceComprometimento
	fields = ['indice', 'descricao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar índices de comprometimento',
		'name_button': 'Atualizar índice de comprometimento',
	}

class PastoralUpdate(LoginRequiredMixin, UpdateView):
	model = Pastoral
	fields = ['nome', 'sigla']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar pastoral',
		'name_button': 'Atualizar pastoral',
	}

class MembroUpdate(LoginRequiredMixin, UpdateView):
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
		'title': 'Atualizar membros',
		'name_button': 'Atualizar membro',
	}

class AtualizacaoMembroUpdate(LoginRequiredMixin, UpdateView):
	model = AtualizacaoMembro
	fields = ['membro', 'data_atualizacao', 'observacao']
	template_name = 'cadastros/form.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Atualizar atualização de membros',
		'name_button': 'Atualizar atualização de membros',
	}

#### DeleteView

class GrupoDelete(LoginRequiredMixin, DeleteView):
	model = Grupo
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir grupo',
		'name_button': 'Excluir grupo',
	}

class TurmaDelete(LoginRequiredMixin, DeleteView):
	model = Turma
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir turma',
		'name_button': 'Excluir turma',
	}

class FuncaoDelete(LoginRequiredMixin, DeleteView):
	model = Funcao
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir função',
		'name_button': 'Excluir função',
	}

class DisponibilidadeDelete(LoginRequiredMixin, DeleteView):
	model = Disponibilidade
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir disponibilidade',
		'name_button': 'Excluir disponibilidade',
	}

class SituacaoDelete(LoginRequiredMixin, DeleteView):
	model = Situacao
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir situação',
		'name_button': 'Excluir situação',
	}

class IndiceComprometimentoDelete(LoginRequiredMixin, DeleteView):
	model = IndiceComprometimento
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir índice de comprometimento',
		'name_button': 'Excluir índice de comprometimento',
	}

class PastoralDelete(LoginRequiredMixin, DeleteView):
	model = Pastoral
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir pastoral',
		'name_button': 'Excluir pastoral',
	}

class MembroDelete(LoginRequiredMixin, DeleteView):
	model = Membro
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir membro',
		'name_button': 'Excluir membro',
	}

class AtualizacaoMembroDelete(LoginRequiredMixin, DeleteView):
	model = AtualizacaoMembro
	template_name = 'cadastros/form-delete.html'
	success_url = reverse_lazy('index')
	extra_context = {
		'title': 'Excluir atualização de membros',
		'name_button': 'Excluir atualização de membros',
	}

#### ListView

class GrupoList(ListView):
	model = Grupo
	template_name = 'listas/grupo.html'

class PastoralList(ListView):
	model = Pastoral
	template_name = 'listas/pastoral.html'

class TurmaList(ListView):
	model = Turma
	template_name = 'listas/turma.html'

class FuncaoList(ListView):
	model = Funcao
	template_name = 'listas/funcao.html'

class DisponibilidadeList(ListView):
	model = Disponibilidade
	template_name = 'listas/disponibilidade.html'

class SituacaoList(ListView):
	model = Situacao
	template_name = 'listas/situacao.html'

class IndiceComprometimentoList(ListView):
	model = IndiceComprometimento
	template_name = 'listas/indice.html'

class MembroList(ListView):
	model = Membro
	template_name = 'listas/membro.html'

	def get_queryset(self):
		return Membro.objects.select_related('grupo', 'turma', 'funcao', 'disponibilidade', 'situacao', 'indice_comprometimento').all()
