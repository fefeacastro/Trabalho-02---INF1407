# Trabalho 02 INF1407

## Participantes
Fernanda Castro e Mariana Salgueiro

## Segundo Trabalho de Programação para Web de 2020/2
Instruções gerais:
* Trabalho individual ou em grupo de até 2 componentes.
* Data da entrega: 02/12/2020.
* Data para apresentação individual: 07-09/12/2020.
ATENÇÃO: antes de desenvolver o site, me envie por email um resumo do que será implementado no site. Esse resumo será utilizado para eu avaliar se o conteúdo está de acordo com o esperado.
Desenvolva um site Web com o conteúdo apresentado em sala de aula:
* Site em Django
* Deve conter as quatro operações básicas em banco de dados (CRUD)
* Deve ser publicado
* Usar Git para controle de versão
* Realizar push semanalmente.
* Como haverá controle de versão e de quem fez o quê pelo Git, as notas dos componentes do grupo podem ser diferentes.
* AJAX
* Login, acesso e/ou ações selecionadas por usuário.
* A entrega deverá ser acompanhada por uma carta relatando o que foi desenvolvido.
Para realizar a entrega:
* Publique o seu site. Me envie o link.
* Disponibilize a última versão integral em um Git. Me envie o link.

## Primeira Instalação
```
conda create --name inf1407 python
activate inf1407
pip install django
pip freeze > requirements.txt
django-admin startproject LojaMariFe
python manage.py migrate
```

## Toda vez que for programar
```
conda activate inf1407
python manage.py runserver (rodar esse comando na mesma pasta que tiver o manage.py)
```
Abrir em algum browser: http://localhost:8000/ <br/>
Toda mudança de interface feita vai ser automaticamente mostrada no browser quando você der refresh nele (f5 ou ctrl + f5 ou até ctrl + shift + r - só tem q ver como é isso pra mac).

## Criando uma nova tabela no banco
```
python manage.py makemigrations project
python manage.py migrate
```