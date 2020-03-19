from django.contrib import admin
from .models import \
    Funcionario, \
    Cargo, \
    Features, \
    Publicacoes, \
    Services, \
    Clientes, \
    Counter


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('title', 'ativo', 'modificado')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo',)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado',)


@admin.register(Publicacoes)
class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('modificado',)
