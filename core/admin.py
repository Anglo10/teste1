from django.contrib import admin
from core.models.cadastro import Pessoa
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nascimento')
    class Meta:
        model = Pessoa

admin.site.register(Pessoa, PessoaAdmin)