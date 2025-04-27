from django.contrib import admin
from .models import Grupo, Turma, Funcao, Disponibilidade, Situacao, Membro, AtualizacaoMembro, IndiceComprometimento
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Grupo)
admin.site.register(Turma)
admin.site.register(Funcao)
admin.site.register(Disponibilidade)
admin.site.register(Situacao)
admin.site.register(Membro)
admin.site.register(AtualizacaoMembro)
admin.site.register(IndiceComprometimento)
