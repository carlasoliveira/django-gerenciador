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
	num_turma = models.IntegerField(unique=True, verbose_name="número da turma", default=0)
	data_investidura = models.DateField(verbose_name="data de investidura")
	grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name="grupo", default=0)
	
	def __str__(self):
		return f"Turma nº {self.num_turma} - {self.grupo.nome}"
	
	class Meta:
		verbose_name = "Turma"
		verbose_name_plural = "Turmas"
		ordering = ['data_investidura']

class Funcao(models.Model):
	funcao = models.CharField(max_length=100, verbose_name="função", unique=True)
	descricao = models.TextField(verbose_name="descrição da função", blank=True, null=True)

	def __str__(self):
		return f"{self.funcao}"
	
	class Meta:
		verbose_name = "Função"
		verbose_name_plural = "Funções"
		ordering = ['funcao']

class Disponibilidade(models.Model):
	dia_semana = models.CharField(max_length=20, verbose_name="Dia e Horário com celebração", unique=True)

	def __str__(self):
		return f"{self.dia_semana}"
	
	class Meta:
		verbose_name = "Disponibilidade"
		verbose_name_plural = "Disponibilidades"
		ordering = ['dia_semana']

class Situacao(models.Model):
	situacao = models.CharField(max_length=20, unique=True)
	descricao = models.TextField(max_length=100, verbose_name="descrição da situação", blank=True, null=True)

	def __str__(self):
		return f"{self.situacao}"
	
	class Meta:
		verbose_name = "Situação"
		verbose_name_plural = "Situações"
		ordering = ['situacao']

class IndiceComprometimento(models.Model):
	indice = models.CharField(max_length=50, unique=True)
	descricao = models.TextField(max_length=100, verbose_name="descrição do índice de comprometimento", blank=True, null=True)

	def __str__(self):
		return f"{self.indice}"
	
	class Meta:
		verbose_name = "Índice de Comprometimento"
		verbose_name_plural = "Índices de Comprometimento"
		ordering = ['indice']

class Pastoral(models.Model):
	nome = models.CharField(max_length=100, unique=True, verbose_name="nome da pastoral")
	sigla = models.CharField(max_length=10, unique=True, verbose_name="sigla da pastoral")
	status = models.BooleanField(default=True, verbose_name="Ativa/Inativa")
	
	def __str__(self):
		return f"{self.sigla}"
	
	class Meta:
		verbose_name = "Pastoral"
		verbose_name_plural = "Pastorais"
		ordering = ['nome']

class Membro(models.Model):
	nome = models.CharField(max_length=100, verbose_name="nome")
	resumo = models.TextField(max_length=300, verbose_name="resumo", blank=True, null=True)
	data_nascimento = models.DateField(verbose_name="data de nascimento")
	telefone = models.CharField(max_length=15, verbose_name="telefone")
	endereco = models.CharField(max_length=200, verbose_name="endereço", blank=True, null=True)
	nome_pai = models.CharField(max_length=100, verbose_name="nome do pai", blank=True, null=True)
	nome_mae = models.CharField(max_length=100, verbose_name="nome da mãe", blank=True, null=True)
	class Sacramentos(models.TextChoices):
		BATISMO = 'B', 'Somente o Batismo'
		EUCARISTIA = 'E', 'Somente a Eucaristia'
		BATISMO_EUCARISTIA = 'BE', 'Batismo e Eucaristia'
		TODOS = 'T', 'Todos concluídos'
	sacramentos = models.CharField(max_length=2, choices=Sacramentos.choices, default=Sacramentos.TODOS, verbose_name="Sacramentos de Iniciação Cristã")
	atuacao_pastorais = models.ForeignKey(Pastoral, on_delete=models.PROTECT,  verbose_name="atuações em pastorais")
	grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name="grupo")
	turma = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="turma")
	funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT, verbose_name="função")
	disponibilidade = models.ManyToManyField(Disponibilidade, verbose_name="disponibilidade")
	situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, verbose_name="situação")
	indice_comprometimento = models.ForeignKey(IndiceComprometimento, on_delete=models.PROTECT, verbose_name="índice de comprometimento")
	usuario = models.OneToOneField(User, on_delete=models.PROTECT)
	observacao = models.TextField(max_length=300, verbose_name="observações", blank=True, null=True)

	def __str__(self):
		return f"{self.nome}"
	
	class Meta:
		verbose_name = "Membro"
		verbose_name_plural = "Membros"
		ordering = ['nome']

class AtualizacaoMembro(models.Model):
	membro = models.ManyToManyField(Membro, verbose_name="membro")
	data_atualizacao = models.DateField(verbose_name="data da atualização", default="2019-08-17")
	observacao = models.TextField(max_length=200, verbose_name="observação", blank=True, null=True)

	def __str__(self):
		return f"{self.membro} - {self.data_atualizacao}"
	
	class Meta:
		verbose_name = "Atualização de Membro"
		verbose_name_plural = "Atualizações de Membros"
		ordering = ['data_atualizacao']