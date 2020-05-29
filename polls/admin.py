from django.contrib import admin

# Register your models here.

from .models import Pergunta, Opcao

class OpcaoInline(admin.StackedInline):
    model = Opcao
    extra = 0

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('pergunta_texto', 'data_publicacao','publicado_recentemente')
    list_filter = ['data_publicacao']
    search_fields = ['pergunta_texto']
    inlines = [OpcaoInline]

admin.site.register(Pergunta, PerguntaAdmin)
