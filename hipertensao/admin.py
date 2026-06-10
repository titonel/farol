from django.contrib import admin
from .models import Paciente, Medicamento, Afericao, AtendimentoMultidisciplinar

admin.site.register(Paciente)
admin.site.register(Medicamento)
admin.site.register(Afericao)
admin.site.register(AtendimentoMultidisciplinar)