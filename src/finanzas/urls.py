from django.urls import path
from . import views

urlpatterns = [
    path('ingresos/', views.lista_ingresos, name='lista_ingresos'),
    path('gastos/', views.lista_gastos, name='lista_gastos'),
    path('balance/', views.balance, name='balance'),
]