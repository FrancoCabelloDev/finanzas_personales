from django.shortcuts import render
from .models import Ingreso, Gasto, Balance

def lista_ingresos(request):
    ingresos = Ingreso.objects.all()
    return render(request, 'finanzas/lista_ingresos.html', {'ingresos': ingresos})

def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'finanzas/lista_gastos.html', {'gastos': gastos})

def balance(request):
    balance = Balance.objects.first()  # Obtener el primer balance (si existe)
    return render(request, 'finanzas/balance.html', {'balance': balance})
