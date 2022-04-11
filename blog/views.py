from django.shortcuts import render
from django.template import loader
from .models import Usuario, Creador, Espectador
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class UsuarioVista(TemplateView):
   template_name = ""
   def get(self, request, status=None):
       Usuariomodel=Usuario.objects.all()
       context= {"Usuario":Usuariomodel}
       return render(request, self.template_name, context)

class CreadorVista(TemplateView):
   template_name = ""
   def get(self, request, status=None):
       Creadormodel=Creador.objects.all()
       context= {"Creador":Creadormodel}
       return render(request, self.template_name, context)

class EspectadorVista(TemplateView):
   template_name = ""
   def get(self, request, status=None):
       Espectadormodel=Espectador.objects.all()
       context= {"Espectador":Espectadormodel}
       return render(request, self.template_name, context)