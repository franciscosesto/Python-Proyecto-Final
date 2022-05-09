from django.contrib import admin
from .models import Usuario, Creador, Espectador, Avatar, Article, ProfileData, Mensajes

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Creador)
admin.site.register(Espectador)
admin.site.register(Avatar)
admin.site.register(Article)
admin.site.register(ProfileData)
admin.site.register(Mensajes)