# src/finanzas/forms.py

from django import forms
from .models import Ingreso, Gasto, Balance

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['descripcion', 'monto', 'fecha']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'fecha']

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['ingresos', 'gastos']  # Los campos deben coincidir con el modelo Balance
