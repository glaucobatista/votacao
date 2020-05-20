from django.contrib import admin

# Register your models here.

from .models import Pergunta, Opcao

admin.site.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    fields = ('pergunta_texto')


admin.site.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    fields = ('opcao_texto', 'votos')
    list_display = ('opcao_texto', 'votos')