# Trabalho 02 INF1407

## Participantes
Fernanda Castro e Mariana Salgueiro

# Para testar o site no ar

## Link
http://lojamarife.herokuapp.com/

## Instruções de uso (Google Chrome)
* Ao acessar o site pela primeira vez faça seu registro
* Faça Login
* Navegue pelo site
* Coloque produtos no carrinho
* Retire produtos do carrinho
* Mude sua senha

# Para testar localmente
* Clone o repositório do GitHub
* Navegue através de um prompt até a pasta clonada
* Execute os seguintes comandos:
```
conda create --name inf1407 python
conda activate inf1407
pip install -r requirements.txt
cd LojaMariFe
python manage.py runserver
```

# Para o desenvolvimento foi necessário

## Primeira instalação
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