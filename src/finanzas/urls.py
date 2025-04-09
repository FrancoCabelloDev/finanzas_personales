from django.urls import path
from . import views

urlpatterns = [
    # Ingresos
    path('ingresos/', views.lista_ingresos, name='lista_ingresos'),
    path('ingresos/crear/', views.crear_ingreso, name='crear_ingreso'),
    path('ingresos/editar/<int:pk>/', views.editar_ingreso, name='editar_ingreso'),
    path('ingresos/eliminar/<int:pk>/', views.eliminar_ingreso, name='eliminar_ingreso'),

    # Gastos
    path('gastos/', views.lista_gastos, name='lista_gastos'),
    path('gastos/crear/', views.crear_gasto, name='crear_gasto'),
    path('gastos/editar/<int:pk>/', views.editar_gasto, name='editar_gasto'),
    path('gastos/eliminar/<int:pk>/', views.eliminar_gasto, name='eliminar_gasto'),

    # Balance
    path('balance/', views.balance, name='balance'),
]
