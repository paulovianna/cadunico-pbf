from django.forms import ModelForm
from workshop.models import Inscricao

class InscricaoForm(ModelForm):
	class Meta:
		model = Inscricao
		fields = ['titulo', 'instituicao', 'orientador', 'participantes', 'area', 'resumo']