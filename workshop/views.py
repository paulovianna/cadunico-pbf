from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from workshop.forms import InscricaoForm
from workshop.models import Inscricao

def Inicio(request):
    ctoken = {}
    ctoken.update(csrf(request))
    if request.method == 'POST':
        form = InscricaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = InscricaoForm()
            return render_to_response('inicio_workshop.html', RequestContext(request,{'form': form, 'token':ctoken, 'inscricao':True}))
        else:
            return render_to_response('inicio_workshop.html', RequestContext(request,{'form': form, 'token':ctoken, 'inscricao':True, 'erro':True}))
    else:
        form = InscricaoForm()
        return render_to_response('inicio_workshop.html', RequestContext(request,{'form': form}))