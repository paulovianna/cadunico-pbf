from django.contrib import admin
from cadunico.models import MunicipioCadUnico

class MunicipioCadUnicoAdmin(admin.ModelAdmin):
     pass
    
admin.site.register(MunicipioCadUnico,MunicipioCadUnicoAdmin)
