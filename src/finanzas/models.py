from django.db import models

class Ingreso(models.Model):
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.descripcion} - {self.monto}'

class Gasto(models.Model):
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.descripcion} - {self.monto}'

class Balance(models.Model):
    ingresos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_balance(self):
        return self.ingresos - self.gastos

    def __str__(self):
        return f'Balance: {self.calcular_balance()}'
