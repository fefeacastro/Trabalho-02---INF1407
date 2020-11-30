from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Produto

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
        produtos.append(Produto.objects.filter(categoria = 'Camisa', pk=i))

    context = {'produtos': produtos, }

    return render(request, 'LojaMariFe/carrinho.html', context=context)


def camisa(request):
    camisas = Produto.objects.filter(categoria = 'Camisa')
    imagens = []
    for camisa in camisas:
        camisa.imagem = str(camisa.imagem)[22:]

    context = {
        'camisas':camisas,
    }

    if request.POST:
        carrinho = request.session.get('carrinho', None)
        if not carrinho:
            carrinho = []
        carrinho.append(request.POST.get('id'))
        request.session['carrinho'] = carrinho

    return render(request, 'LojaMariFe/camisa.html', context=context)


def calca(request):
    calcas = Produto.objects.filter(categoria = 'Calça')
    imagens = []
    for calca in calcas:
        calca.imagem = str(calca.imagem)[22:]
    context = {'calcas':calcas,}
    # TO DO:
    # carrinho
    return render(request, 'LojaMariFe/calca.html', context=context)


def sapato(request):
    sapatos = Produto.objects.filter(categoria = 'Sapato')
    imagens = []
    for sapato in sapatos:
        sapato.imagem = str(sapato.imagem)[22:]
    context = {'sapatos':sapatos,}
    # TO DO:
    # carrinho
    return render(request, 'LojaMariFe/sapato.html', context=context)


def vestido(request):
    vestidos = Produto.objects.filter(categoria = 'Vestido')
    imagens = []
    for vestido in vestidos:
        vestido.imagem = str(vestido.imagem)[22:]
    context = {'vestidos':vestidos,}
    # TO DO:
    # carrinho
    return render(request, 'LojaMariFe/vestido.html', context=context)
