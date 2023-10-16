from django.contrib import admin
from .models import Aeropuerto, Vuelo, Pasajero

# Register your models here.

admin.site.register(Aeropuerto)
admin.site.register(Vuelo)
admin.site.register(Pasajero)
