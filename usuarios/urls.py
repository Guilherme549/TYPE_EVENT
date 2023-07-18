from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
]
