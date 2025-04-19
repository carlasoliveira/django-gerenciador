from django.db import models

#from django.db.models.fields import CharField, DateField, IntegerField, TextField
#from django.db.models.fields.related import ForeignKey, OneToOneField

from django.contrib.auth.models import User
# Create your models here.

class Grupo(models.Model):
	nome = models.CharField(max_length=100, unique=True)
	padroeiro = models.CharField(max_length=100, verbose_name="padroeiro do grupo")
	quantidade_membros = models.IntegerField(default=0, verbose_name="quantidade de membros")

	#Equivalente ao toString para imprimir objetos
	def __str__(self):
		return f"{self.nome}"
	
	class Meta:
		verbose_name = "Grupo"
		verbose_name_plural = "Grupos"
		ordering = ['nome']

class Turma(models.Model):
	data_investidura = models.DateField(verbose_name="data de investidura")
	
	def __str__(self):
		return f"{self.data_investidura}"
	
	class Meta:
		verbose_name = "Turma"
		verbose_name_plural = "Turmas"
		ordering = ['data_investidura']

class Funcao(models.Model):
	funcao = models.CharField(max_length=100, unique=True)
	descricao = models.TextField(verbose_name="descrição da função")

	def __str__(self):
		return f"{self.funcao}"
	
	class Meta:
		verbose_name = "Função"
		verbose_name_plural = "Funções"
		ordering = ['funcao']

class Disponibilidade(models.Model):
	dia_semana = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return f"{self.dia_semana}"
	
	class Meta:
		verbose_name = "Disponibilidade"
		verbose_name_plural = "Disponibilidades"
		ordering = ['dia_semana']

class Situacao(models.Model):
	situacao = models.CharField(max_length=20, unique=True)
	descricao = models.TextField(max_length=100, verbose_name="descrição da situação")

	def __str__(self):
		return f"{self.situacao}"
	
	class Meta:
		verbose_name = "Situação"
		verbose_name_plural = "Situações"
		ordering = ['situacao']

class IndiceComprometimento(models.Model):
	indice = models.CharField(max_length=50, unique=True)
	descricao = models.TextField(max_length=100, verbose_name="descrição do índice de comprometimento")

	def __str__(self):
		return f"{self.indice}"
	
	class Meta:
		verbose_name = "Índice de Comprometimento"
		verbose_name_plural = "Índices de Comprometimento"
		ordering = ['indice']

class Atualizacao(models.Model):
	data_atualizacao = models.DateField(verbose_name="data da atualização")

	def __str__(self):
		return f"{self.data_atualizacao}"
	
	class Meta:
		verbose_name = "Atualização"
		verbose_name_plural = "Atualizações"
		ordering = ['data_atualizacao']

class Membro(models.Model):
	nome = models.CharField(max_length=100, verbose_name="nome")
	resumo = models.TextField(max_length=300, verbose_name="resumo")
	data_nascimento = models.DateField(verbose_name="data de nascimento")
	telefone = models.CharField(max_length=15, verbose_name="telefone")
	endereco = models.CharField(max_length=200, verbose_name="endereço")
	nome_pai = models.CharField(max_length=100, verbose_name="nome do pai")
	nome_mae = models.CharField(max_length=100, verbose_name="nome da mãe")
	sacramentos_recebidos = models.CharField(max_length=200, verbose_name="sacramentos recebidos")
	atuacao_pastorais = models.CharField(max_length=200, verbose_name="atuações em pastorais ")
	grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name="grupo ")
	turma = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="turma ")
	funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT, verbose_name="função ")
	disponibilidade = models.ForeignKey(Disponibilidade, on_delete=models.PROTECT, verbose_name="disponibilidade ")
	situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, verbose_name="situação ")
	indice_comprometimento = models.ForeignKey(IndiceComprometimento, on_delete=models.PROTECT, verbose_name="índice de comprometimento ")
	usuario = models.OneToOneField(User, on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.nome}"
	
	class Meta:
		verbose_name = "Membro"
		verbose_name_plural = "Membros"
		ordering = ['nome']

class AtualizacaoMembro(models.Model):
	membro = models.ForeignKey(Membro, on_delete=models.PROTECT, verbose_name="membro")
	atualizacao = models.ForeignKey(Atualizacao, on_delete=models.PROTECT, verbose_name="atualização")
	observacao = models.TextField(max_length=200, verbose_name="observação")

	def __str__(self):
		return f"{self.membro} - {self.atualizacao}"
	
	class Meta:
		verbose_name = "Atualização de Membro"
		verbose_name_plural = "Atualizações de Membros"
		ordering = ['membro']