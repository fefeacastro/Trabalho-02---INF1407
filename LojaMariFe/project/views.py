from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
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
    return render(request, 'LojaMariFe/carrinho.html', context=None)


def camisa(request):
    return render(request, 'LojaMariFe/camisa.html', context=None)


def calca(request):
    return render(request, 'LojaMariFe/calca.html', context=None)
