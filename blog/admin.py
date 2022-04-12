from django.contrib import admin
from .models import Usuario, Creador, Espectador

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Creador)
admin.site.register(Espectador)

