from django.contrib import admin
from workshop.models import Inscricao

class InscricaoAdmin(admin.ModelAdmin):
     list_display = ('titulo', 'instituicao')

admin.site.register(Inscricao,InscricaoAdmin)	