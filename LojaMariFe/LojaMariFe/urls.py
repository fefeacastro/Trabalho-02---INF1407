"""LojaMariFe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls.base import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(template_name='Auth/login.html'), name='login'),
    path('accounts/profile/', views.carrinho, name='carrinho'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='Auth/password_change_form.html', success_url=reverse_lazy('password_change_done')), name='password_change'),
    path('accounts/password_change_done/', PasswordChangeDoneView.as_view(template_name='Auth/password_change_done.html'), name='password_change_done'),
    path('categoria1/', views.categoria1, name='categoria1')
]

