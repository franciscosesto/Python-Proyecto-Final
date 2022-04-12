from django.shortcuts import render
from django.template import loader
from .models import Usuario, Creador, Espectador
from django.http import HttpResponse
from django.views.generic import TemplateView
from blog.forms import Usuario_Formulario, Creador_Formulario, Espectador_Formulario

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

class HomeVista(TemplateView):
   template_name = "home.html"
   def get(self, request, status=None):
       context= {}
       return render(request, self.template_name, context)

class Usuario_Vista_Forms(TemplateView):
    template_name= 'forms/usuario_forms.html'
    def get(self, request, status=None):
        context={"form": Usuario_Formulario()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= Usuario_Formulario(request.POST)
      if miform.is_valid():
        info= miform.cleaned_data
        name=  info['name'] 
        lastname= info['lastname']
        nickname= info['nickname']
        password= info['password']
        email=  info['email'] 
        age=  info['age']
        var_1 = Usuario(name=name,  lastname=lastname, nickname=nickname, password=password, email=email, age=age)
        var_1.save()
        return render(request, self.template_name)
      else:
          miform=Usuario_Formulario()
      context={'form':Usuario_Formulario()}
      return render(request,self.template_name, context)

class Creador_Vista_Forms(TemplateView):
    template_name= 'forms/creador_forms.html'
    def get(self, request, status=None):
        context={"form": Creador_Formulario()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= Creador_Formulario(request.POST)
      if miform.is_valid():
        info= miform.cleaned_data
        name=  info['name'] 
        lastname= info['lastname']
        nickname= info['nickname']
        password= info['password']
        email=  info['email'] 
        age=  info['age']
        var_1 = Creador(name=name,  lastname=lastname, nickname=nickname, password=password, email=email, age=age)
        var_1.save()
        return render(request, self.template_name)
      else:
          miform=Creador_Formulario()
      context={'form':Creador_Formulario()}
      return render(request,self.template_name, context)

class Espectador_Vista_Forms(TemplateView):
    template_name= 'forms/espectador_forms.html'
    def get(self, request, status=None):
        context={"form": Espectador_Formulario()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= Espectador_Formulario(request.POST)
      if miform.is_valid():
        info= miform.cleaned_data
        name=  info['name'] 
        age=  info['age']
        var_1 = Espectador(name=name, age=age)
        var_1.save()
        return render(request, self.template_name)
      else:
          miform=Espectador_Formulario()
      context={'form':Espectador_Formulario()}
      return render(request,self.template_name, context)



class Creador_Busqueda(TemplateView):
    template_name="busqueda/creador_busqueda.html"
    def get(self, request, status=None):
        context={}
        return render(request, self.template_name, context)

def buscar_modelo_creador(request):
    if request.GET["nickname"]:
        nickname= request.GET["nickname"]
        creador= Creador.objects.filter(nickname__icontains=nickname)
        context= {"Creador": creador, "nickname": nickname}
        return render(request, "busqueda/result_busq_creador.html", context)
    else:
        response = "No enviaste datos"
    return HttpResponse(response)