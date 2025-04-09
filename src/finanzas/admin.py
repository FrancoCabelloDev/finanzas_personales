from django.contrib import admin
from .models import Ingreso, Gasto, Balance

admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Balance)
