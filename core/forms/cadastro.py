from django.forms import ModelForm
from core.models.cadastro import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['']