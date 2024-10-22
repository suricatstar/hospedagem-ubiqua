from django.contrib import admin

from acomodacao.models import *

@admin.register(TipoAcomodacao)
class TipoAcomodacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Estrela)
class EstrelaAdmin(admin.ModelAdmin):
    list_display = ('quantidade',)

@admin.register(Acomodacao)
class AcomodacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'capacidade', 'tipo', 'estrelas')

@admin.register(TipoQuarto)
class TipoQuartoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(AcomodacaoQuarto)
class AcomodacaoQuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'quantidade_pessoas', 'descricao', 'diaria', 'tipo', 'acomodacao')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('acomodacao', 'data_inicio', 'hora_inicio', 'data_fim', 'hora_final', 'quantidade_pessoas', 'valor')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')