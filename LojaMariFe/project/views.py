from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Produto
from .utils import ajeitaCaminhoImagens, addNoCarrinho
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        #cookie habilitado
        request.session.delete_test_cookie()
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


@login_required
def carrinho(request):
    produtos = [] 
    for i in request.session.get('carrinho', None):
        produtos.append(Produto.objects.filter(pk=i))

    preco = 0.0
    for produto in produtos:
        ajeitaCaminhoImagens(produto)
        preco += float(produto[0].preco)

    context = {'produtos': produtos, 
        'preco': preco}

    return render(request, 'LojaMariFe/carrinho.html', context=context)


def camisa(request):
    camisas = Produto.objects.filter(categoria = 'Camisa')

    ajeitaCaminhoImagens(camisas)

    context = {
        'camisas':camisas,
    }

    if request.POST:
        addNoCarrinho(request)

    return render(request, 'LojaMariFe/camisa.html', context=context)


def calca(request):
    calcas = Produto.objects.filter(categoria = 'Calça')

    ajeitaCaminhoImagens(calcas)

    context = {'calcas':calcas,}
    
    if request.POST:
        addNoCarrinho(request)

    return render(request, 'LojaMariFe/calca.html', context=context)


def sapato(request):
    sapatos = Produto.objects.filter(categoria = 'Sapato')

    ajeitaCaminhoImagens(sapatos)

    context = {'sapatos':sapatos,}
    
    if request.POST:
        addNoCarrinho(request)

    return render(request, 'LojaMariFe/sapato.html', context=context)


def vestido(request):
    vestidos = Produto.objects.filter(categoria = 'Vestido')

    ajeitaCaminhoImagens(vestidos)

    context = {'vestidos':vestidos,}
    
    if request.POST:
        addNoCarrinho(request)

    return render(request, 'LojaMariFe/vestido.html', context=context)


def atualizaEstoque(request):
    produto = Produto.objects.get(pk=request.GET.get('produto'))

    produto.quantidade = int(produto.quantidade) - 1
    produto.save() 

    resposta = {'qtd': produto.quantidade, }
    return JsonResponse(resposta)