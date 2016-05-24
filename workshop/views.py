from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from workshop.forms import InscricaoForm

def Inicio(request):
    ctoken = {}
    ctoken.update(csrf(request))
    if request.method == 'POST':
        form = InscricaoForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.handle(request.FILES['file_obj'])
            form = IncricaoForm()
            return render_to_response('inicio_workshop.html', 
                                      RequestContext(request,{'form': form, 'token':ctoken}))
    else:
        form = InscricaoForm()
    return render_to_response('inicio_workshop.html', 
                              RequestContext(request,{'form': form}))