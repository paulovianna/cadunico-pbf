from django.contrib import admin
from cadunico.models import MunicipioCadUnico, MunicipioBeneficiado, EstadoBeneficiado, PaisBeneficiado

class MunicipioCadUnicoAdmin(admin.ModelAdmin):
     pass

class MunicipioBeneficiadoAdmin(admin.ModelAdmin):
     list_display = ('municipio', 'pessoas_cadunico_d')

class EstadoBeneficiadoAdmin(admin.ModelAdmin):
     pass

class PaisBeneficiadoAdmin(admin.ModelAdmin):
     pass
    
admin.site.register(MunicipioCadUnico,MunicipioCadUnicoAdmin)
admin.site.register(MunicipioBeneficiado,MunicipioBeneficiadoAdmin)
admin.site.register(EstadoBeneficiado,EstadoBeneficiadoAdmin)
admin.site.register(PaisBeneficiado,PaisBeneficiadoAdmin)
