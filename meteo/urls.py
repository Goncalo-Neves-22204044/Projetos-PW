from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    
    path('previsao-lisboa/', views.previsao_lisboa_view, name='previsao_lisboa'),
    
    path('previsao/', views.previsao, name='previsao'),
    
    path('previsao/<int:city_id>/', views.previsao_cidade, name='previsao_cidade'),
    path('api/listacidades/', views.cidades_view, name='cidadesAPI'),
    path('api/tempo/<int:city_id>/', views.tempo_cidade, name='tempo_cidade'),
]