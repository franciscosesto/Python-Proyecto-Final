from django.urls import path
from .views import  Creador_Busqueda, HomeVista, Usuario_Vista_Forms, Creador_Vista_Forms, Espectador_Vista_Forms, Creador_Busqueda, buscar_modelo_creador


urlpatterns = [
path("", HomeVista.as_view(), name="inicio"),
path("usuarioforms/", Usuario_Vista_Forms.as_view(), name="usuarioforms"),
path("creadorforms/", Creador_Vista_Forms.as_view(), name="creadorforms"),
path("espectadorforms/", Espectador_Vista_Forms.as_view(), name="espectadorforms"),
path("creadorsearch/", Creador_Busqueda.as_view(), name="creadorsearch"),
path("buscar_creador/", buscar_modelo_creador, name="buscarmodelocreador"),
]
