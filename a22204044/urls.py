"""a22204044 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('mebyme', views.mebyme_view, name='mebyme'),
    path('about', views.about_view, name='about'),
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/', include('pwsite.urls')),
    path('bands/', include('bandas.urls')),
    path('articles/', include('articles.urls')),
    path('filmes/', include('filmes.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('curso/', include('curso.urls')),
    path('meteo/', include('meteo.urls'))
]
