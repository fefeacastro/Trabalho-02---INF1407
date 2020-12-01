from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Produto
from django.http import JsonResponse
import json

# Create your views here.
def homepage(request):
    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        #cookie habilitado
        request.session.delete_test_cookie()
        if not request.session.get('carrinho', None):
            request.session['carrinho'] = []
    else:
        return render(request, 'LojaMariFe/semCookies.html', context=None)

    return render(request, 'LojaMariFe/homepage.html', context=None)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            context = {'form':form,}
            return render(request, 'Auth/register.html', context)
    else:
        form = CustomUserCreationForm()
        context = {'form':form,}
        return render(request, 'Auth/register.html', context)


def produtos(request, tipo):
    if request.POST:
        carrinho = request.session.get('carrinho', None)
        if not carrinho:
            carrinho = []
        carrinho.append(request.POST.get('id'))
        request.session['carrinho'] = carrinho

    produtos = Produto.objects.filter(categoria = tipo)

    for prod in produtos:
        prod.imagem = str(prod.imagem)[22:]

    ids = []
    for i in Produto.objects.all().values('pk'):
        ids.append(i['pk'])

    context = {
        'produtos':produtos,
        'title':tipo,
        'ids':json.dumps(ids, default=lambda obj: obj.__dict__),
    }

    return render(request, 'LojaMariFe/produtos.html', context=context)


@login_required
def carrinho(request):
    produtos = [] 
    for i in request.session.get('carrinho', None):
        produtos.append(Produto.objects.get(pk=i))

    dict_produtos = {}
    preco = 0.0

    for prod in produtos:
        if prod in dict_produtos:
            dict_produtos[prod] += 1
        else:
            dict_produtos[prod] = 1
        
        preco += float(prod.preco) 

    for prod in produtos:
        prod.imagem = str(prod.imagem)[22:]

    context = {
        'produtos': dict_produtos, 
        'preco': float("{:.2f}".format(preco))
    }

    return render(request, 'LojaMariFe/carrinho.html', context=context)


def atualizaEstoque(request):
    produto = Produto.objects.get(pk=request.GET.get('produto'))

    if produto.quantidade > 0:
        produto.quantidade = int(produto.quantidade) - 1

    produto.save()

    resposta = {
        'qtd': produto.quantidade, 
        'id': produto.pk, 
    }
    return JsonResponse(resposta)