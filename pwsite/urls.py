from django.urls import path
from . import views

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('interests/', views.interests_view, name='interests')
]