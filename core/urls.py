from django.urls import path
from . import views
from . import views_admin

urlpatterns = [
    # Autenticação
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('trocar-senha/', views.trocar_senha_view, name='trocar_senha'),
    
    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Menu de Cadastros
    path('cadastro/', views.cadastro_menu_view, name='cadastro_menu'),
    
    # Usuários
    path('usuarios/', views.usuario_lista_view, name='usuario_lista'),
    path('usuarios/novo/', views.usuario_criar_view, name='usuario_criar'),
    
    # Empresas
    path('empresas/', views.empresa_lista_view, name='empresa_lista'),
    path('empresas/nova/', views.empresa_criar_view, name='empresa_criar'),
    path('empresas/<int:pk>/editar/', views.empresa_editar_view, name='empresa_editar'),
    
    # Médicos
    path('medicos/', views.medico_lista_view, name='medico_lista'),
    path('medicos/novo/', views.medico_criar_view, name='medico_criar'),
    path('medicos/<int:pk>/editar/', views.medico_editar_view, name='medico_editar'),
    
    # ========== ÁREA ADMINISTRATIVA (TIER 5) ==========
    
    # Menu Admin
    path('admin/', views_admin.admin_menu_view, name='admin_menu'),
    
    # Cirurgias
    path('admin/cirurgias/', views_admin.cirurgia_lista_view, name='cirurgia_lista'),
    path('admin/cirurgias/nova/', views_admin.cirurgia_criar_view, name='cirurgia_criar'),
    path('admin/cirurgias/<int:pk>/editar/', views_admin.cirurgia_editar_view, name='cirurgia_editar'),
    path('admin/cirurgias/upload-csv/', views_admin.cirurgia_upload_csv_view, name='cirurgia_upload_csv'),
    path('admin/cirurgias/buscar-sigtap/', views_admin.buscar_sigtap_view, name='buscar_sigtap'),
    
    # Exames
    path('admin/exames/', views_admin.exame_lista_view, name='exame_lista'),
    
    # Serviços Médicos
    path('admin/servicos/', views_admin.servico_lista_view, name='servico_lista'),
]
