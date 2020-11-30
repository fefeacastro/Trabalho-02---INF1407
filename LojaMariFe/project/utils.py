#Funcoes auxiliares usadas no projeto
def ajeitaCaminhoImagens(produtos):
    for prod in produtos:
        prod.imagem = str(prod.imagem)[22:]

    return produtos

def addNoCarrinho(request):
    carrinho = request.session.get('carrinho', None)
    if not carrinho:
        carrinho = []
    carrinho.append(request.POST.get('id'))
    request.session['carrinho'] = carrinho