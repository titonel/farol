from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps
from . import views
from . import views_home

app_name = "cadastro"

def farol_login_required(view_func):
    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.primeiro_acesso:
            return redirect('trocar_senha')
        return view_func(request, *args, **kwargs)
    return wrapper

urlpatterns = [
    # ── Landing page ──────────────────────────────────────────────────────────
    path("", farol_login_required(views_home.home), name="home"),

    # ── Módulo: Acompanhamento de Produção ────────────────────────────────────
    path("acompanhamento/", farol_login_required(views_home.acompanhamento), name="acompanhamento"),

    # ── Módulo: Relatório ─────────────────────────────────────────────────────
    path("relatorio/", farol_login_required(views_home.relatorio), name="relatorio"),
    path("relatorio/<int:pk>/download/", farol_login_required(views_home.relatorio_download), name="relatorio_download"),

    # ── Módulo: Indicadores ───────────────────────────────────────────────────
    path("indicadores/", farol_login_required(views_home.indicadores), name="indicadores"),
    path("indicadores/prestador/", farol_login_required(views_home.indicadores_prestador), name="indicadores_prestador"),
    path("indicadores/especialidade/", farol_login_required(views_home.indicadores_especialidade), name="indicadores_especialidade"),

    # ── Módulo: Cadastro — Prestadores ────────────────────────────────────────
    path("prestadores/", farol_login_required(views.prestador_list), name="prestador_list"),
    path("prestadores/novo/", farol_login_required(views.prestador_create), name="prestador_create"),
    path("prestadores/<int:pk>/", farol_login_required(views.prestador_detail), name="prestador_detail"),
    path("prestadores/<int:pk>/editar/", farol_login_required(views.prestador_edit), name="prestador_edit"),
    path("prestadores/<int:pk>/excluir/", farol_login_required(views.prestador_delete), name="prestador_delete"),

    # ── Diagnóstico temporário ────────────────────────────────────────────────
    path("diagnostico/producao/", farol_login_required(views_home.diagnostico_producao), name="diagnostico_producao"),

    # ── Módulo: Cadastro — Médicos ────────────────────────────────────────────
    path("medicos/", farol_login_required(views.medico_list), name="medico_list"),
    path("medicos/novo/", farol_login_required(views.medico_create), name="medico_create"),
    path("medicos/<int:pk>/", farol_login_required(views.medico_detail), name="medico_detail"),
    path("medicos/<int:pk>/editar/", farol_login_required(views.medico_edit), name="medico_edit"),
    path("medicos/<int:pk>/excluir/", farol_login_required(views.medico_delete), name="medico_delete"),

    # ── Módulo: Mapeamento de Agendas ─────────────────────────────────────────
    path("prestadores/<int:prestador_pk>/mapeamentos/", farol_login_required(views.mapeamento_list), name="mapeamento_list"),
    path("agendas/autocomplete/", farol_login_required(views.agendas_autocomplete), name="agendas_autocomplete"),

    # ── Módulo: Cadastro — Importação de Contratos via PDF ────────────────────
    path("contrato/upload/", farol_login_required(views.contrato_upload), name="contrato_upload"),
    path("contrato/<int:pk>/revisar/", farol_login_required(views.contrato_revisao), name="contrato_revisao"),
    path("contrato/<int:pk>/ignorar/", farol_login_required(views.contrato_ignorar), name="contrato_ignorar"),
]
