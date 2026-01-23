from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Empresa, Medico


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'nome_completo', 'email', 'tier', 'primeiro_acesso', 'is_active']
    list_filter = ['tier', 'primeiro_acesso', 'is_active', 'is_staff']
    search_fields = ['username', 'nome_completo', 'email', 'cpf']
    ordering = ['-data_cadastro']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'email', 'cpf', 'drt')}),
        ('Permissões', {'fields': ('tier', 'primeiro_acesso', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nome_completo', 'cpf', 'tier', 'password1', 'password2'),
        }),
    )


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['razao_social', 'nome_fantasia', 'cnpj', 'ativa', 'data_cadastro']
    list_filter = ['ativa', 'data_cadastro']
    search_fields = ['razao_social', 'nome_fantasia', 'cnpj']
    readonly_fields = ['data_cadastro', 'data_atualizacao', 'cadastrado_por']
    ordering = ['razao_social']


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'crm', 'especialidade', 'ativo', 'data_cadastro']
    list_filter = ['ativo', 'especialidade', 'data_cadastro']
    search_fields = ['nome_completo', 'crm', 'cpf']
    readonly_fields = ['data_cadastro', 'data_atualizacao', 'cadastrado_por']
    ordering = ['nome_completo']
