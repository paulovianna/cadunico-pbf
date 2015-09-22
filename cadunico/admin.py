from django.contrib import admin
from cadunico.models import MunicipioCadUnico, MunicipioBeneficiado

class MunicipioCadUnicoAdmin(admin.ModelAdmin):
     pass

class MunicipioBeneficiadoAdmin(admin.ModelAdmin):
     pass
    
admin.site.register(MunicipioCadUnico,MunicipioCadUnicoAdmin)
admin.site.register(MunicipioBeneficiado,MunicipioBeneficiadoAdmin)
