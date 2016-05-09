from django.shortcuts import render_to_response
from django.template import RequestContext

def Inicio(request):

     return render_to_response('inicio_grupo_pesquisa.html', RequestContext(request,{}))