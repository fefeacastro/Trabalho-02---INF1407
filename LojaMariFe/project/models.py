from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do produto')
    descricao = models.CharField(max_length=250, help_text='Descrição do produto')
    preco = models.DecimalField(decimal_places=2, max_digits=10, help_text='Preço do produto')
    quantidade = models.IntegerField(help_text='Quantidade de produto em estoque')
    imagem = models.ImageField(help_text='Imagem do produto')
    categoria = models.CharField(max_length=250, help_text='Categoria do produto')

    def __str__(self):
        return self.nome