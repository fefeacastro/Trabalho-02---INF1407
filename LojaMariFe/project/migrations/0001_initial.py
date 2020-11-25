# Generated by Django 3.1.3 on 2020-11-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do produto', max_length=100)),
                ('descricao', models.CharField(help_text='Descrição do produto', max_length=250)),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço do produto', max_digits=10)),
                ('quantidade', models.IntegerField(help_text='Quantidade de produto em estoque')),
                ('imagem', models.ImageField(help_text='Imagem do produto', upload_to='')),
                ('categoria', models.CharField(choices=[('Camisa', 'Camisa'), ('Calça', 'Calça'), ('Sapato', 'Sapato'), ('Vestido', 'Vestido')], help_text='Categoria do produto', max_length=50)),
            ],
        ),
    ]
