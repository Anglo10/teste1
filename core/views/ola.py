from django.shortcuts import render, redirect
from core.forms.cadastro import PessoaForm
from core.models.cadastro import Pessoa
from django.http import HttpResponse

def saudacao(request):
    dados = {}
    dados['form'] = PessoaForm()
    dados['lista'] = Pessoa.objects.all()
    return render(request, 'core/index.html', dados)

def adeus(request):
    return render(request, 'core/retorno.html')

def nova_pessoa(request):
    pessoa = PessoaForm(request.POST)

    if  pessoa.is_valid:
        pessoa.save()
        return redirect('saudacao')
    return ('flw')

#Recupera os dados da pessoa
def atualizar_pessoa(request, pk):
    dados = {}
    pessoa = Pessoa.objects.get(id=pk)
    dados['form'] = PessoaForm(instance=pessoa)
    dados['pk'] = pk
    return render(request, 'core/atualizar_pessoa.html', dados)
#Atualiza a pessoa no banco
def pessoa_atualizada(request):
    pessoa = Pessoa.objects.get(pk=request.POST['id_pessoa'])
    form = PessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid:
        form.save()
        return redirect('saudacao')

def delete_pessoa(request, pk):
    pessoa = Pessoa.objects.get(id=pk)
    pessoa.delete()
    return redirect('saudacao')