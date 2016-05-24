from django.contrib import admin
from workshop.models import Inscricao

class InscricaoAdmin(admin.ModelAdmin):
     pass

admin.site.register(Inscricao,InscricaoAdmin)