from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingreso, Gasto, Balance
from .forms import IngresoForm, GastoForm, BalanceForm

# Ingresos
def lista_ingresos(request):
    ingresos = Ingreso.objects.all()
    return render(request, 'finanzas/lista_ingresos.html', {'ingresos': ingresos})

def crear_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ingresos')
    else:
        form = IngresoForm()
    return render(request, 'finanzas/crear_ingreso.html', {'form': form})

def editar_ingreso(request, pk):
    ingreso = get_object_or_404(Ingreso, pk=pk)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('lista_ingresos')
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, 'finanzas/editar_ingreso.html', {'form': form})

def eliminar_ingreso(request, pk):
    ingreso = get_object_or_404(Ingreso, pk=pk)
    ingreso.delete()
    return redirect('lista_ingresos')

# Gastos
def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'finanzas/lista_gastos.html', {'gastos': gastos})

def crear_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')
    else:
        form = GastoForm()
    return render(request, 'finanzas/crear_gasto.html', {'form': form})

def editar_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'finanzas/editar_gasto.html', {'form': form})

def eliminar_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    gasto.delete()
    return redirect('lista_gastos')

# Balance
def balance(request):
    balance = Balance.objects.first()  # Obtener el primer balance (si existe)
    return render(request, 'finanzas/balance.html', {'balance': balance})
