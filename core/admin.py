from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'nome_completo', 'email', 'tier', 'tipo_profissional', 'registro_profissional', 'primeiro_acesso', 'is_active']
    list_filter = ['tier', 'tipo_profissional', 'primeiro_acesso', 'is_active', 'is_staff']
    search_fields = ['username', 'nome_completo', 'email', 'cpf', 'registro_profissional']
    ordering = ['-data_cadastro']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'email', 'cpf', 'drt')}),
        ('Dados Profissionais (Saúde)', {'fields': ('tipo_profissional', 'tipo_registro', 'registro_profissional')}),
        ('Controle de Acesso', {'fields': ('tier', 'primeiro_acesso', 'mudar_senha', 'email_verificado')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nome_completo', 'cpf', 'tier', 'password1', 'password2'),
        }),
    )
