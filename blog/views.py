from pipes import Template
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import Usuario, Creador, Espectador, Article, Avatar, ProfileData, Mensajes
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import Usuario_Formulario, Creador_Formulario, Espectador_Formulario, ArticleForm, AvatarForm, UserUpdateForm, ProfileDataForm, MensajesForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm



# Create your views here.

#-------- Sección de primer entrega-----------
class UsuarioVista(TemplateView):
   template_name = "l"
   def get(self, request, status=None):
       Usuariomodel=Usuario.objects.all()
       context= {"Usuarios":Usuariomodel}
       return render(request, self.template_name, context)

class CreadorVista(LoginRequiredMixin, TemplateView):
   template_name = "models/creador.html"
   def get(self, request, status=None):
       Creadormodel=Creador.objects.all()
       context= {"Creadores":Creadormodel}
       return render(request, self.template_name, context)

class EspectadorVista(TemplateView):
   template_name = ""
   def get(self, request, status=None):
       Espectadormodel=Espectador.objects.all()
       context= {"Espectadores":Espectadormodel}
       return render(request, self.template_name, context)


#-------- Sección de páginas principales-----------
class HomeVista(TemplateView):
   template_name = "home.html"
   def get(self, request, status=None):
       context= {}
       return render(request, self.template_name, context)

class AboutVista(TemplateView):
   template_name = "about.html"
   def get(self, request, status=None):
       context= {}
       return render(request, self.template_name, context)

class ContactVista(TemplateView):
   template_name = "contact.html"
   def get(self, request, status=None):
       context= {}
       return render(request, self.template_name, context)

class AgradecimientosVista(TemplateView):
   template_name = "agradecimientos.html"
   def get(self, request, status=None):
       context= {}
       return render(request, self.template_name, context)

#-------- Sección de perfiles-----------

class ProfileVista(LoginRequiredMixin, TemplateView):
   template_name = "profile.html"
   def get(self, request, status=None):
       user= self.request.user
       try:
           avatar= Avatar.objects.get(user=user.id).image.url
       except Exception as e :
           print(type(e).__name__)
           avatar=False 
       try:
           profile_data= ProfileData.objects.get(user=user.id)
       except Exception as e :
           print(type(e).__name__)
           profile_data=False    
       try:
           profile_data_pk= ProfileData.objects.get(user=self.request.user).pk
       except Exception as e :
           print(type(e).__name__)
           profile_data_pk=False  
       try:
           pk_avatar=Avatar.objects.get(user=self.request.user).pk
       except Exception as e :
           print(type(e).__name__)
           pk_avatar=False 
       context= {"username":user.username, "email":user.email,"name":user.first_name, "lastname":user.last_name, "avatar": avatar,
       "pk_avatar":pk_avatar, "profile_data":profile_data,"pk_profile_data":profile_data_pk}
       return render(request, self.template_name, context)

class ProfileUpdateView(LoginRequiredMixin,TemplateView):
    template_name= "update/profile_update.html"
    

    def get(self, request):
        user=self.request.user
        context={"form": UserUpdateForm(initial={"username":user.username, "email":user.email,
                                                 "first_name":user.first_name, "last_name":user.last_name})}
        return render(request, self.template_name, context)

    
    def post(self, request):
        form=UserUpdateForm(request.POST)
        user=self.request.user

        if form.is_valid():
          info=form.cleaned_data
          user.email= info.get("email")
          user.first_name= info.get("first_name")
          user.last_name= info.get("last_name")
          user.save()
          print("se guardó")
        print(form.errors)
        return redirect("/accounts/profile")
        




        # context={"form": UserRegisterForm()}
        # return render(request, self.template_name, context)


class ProfileDataCreateView(LoginRequiredMixin, TemplateView):
    template_name="forms/avatar_forms.html"
    def get(self, request, status=None):
        context={"form": ProfileDataForm()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= ProfileDataForm(request.POST)
      if miform.is_valid():
        info= miform.cleaned_data
        Descripción=  info['Descripción']
        Link=  info['Link']
        var_1 = ProfileData(Descripción=Descripción,Link=Link, user=self.request.user)
        var_1.save()
        print("to gucci")
        # return render(request, self.template_name) este no
        return redirect('/accounts/profile')
      else:
          print(miform.errors)
          miform=ProfileDataForm()
          print("algo raro está pasando")
          
      context={'form':ProfileDataForm()}
      return render(request,self.template_name, context)

class ProfileDataUpdateView(LoginRequiredMixin, UpdateView):
    template_name="update/update_profile_data.html"
    model=ProfileData
    success_url= '/accounts/profile'
    fields=['Descripción', 'Link']

    def get_object(self):
        return ProfileData.objects.get(user=self.request.user)

#-------- Sección de Mensajes-----------
class MensajesVista(ListView):
    model= Mensajes
    template_name="models/mensajes.html"

class CrearMensajesVista(LoginRequiredMixin, TemplateView):
    template_name="forms/avatar_forms.html"
    def get(self, request, status=None):
        context={"form": MensajesForm()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= MensajesForm(request.POST)
      if miform.is_valid():
        info= miform.cleaned_data
        mensaje=  info['mensaje']
        var_1 = Mensajes(mensaje=mensaje, user=self.request.user)
        var_1.save()
        print("to gucci")
        # return render(request, self.template_name) este no
        return redirect('/messages/')
      else:
          print(miform.errors)
          miform=MensajesForm()
          print("algo raro está pasando")
          
      context={'form':MensajesForm()}
      return render(request,self.template_name, context)
#-------- Sección de Pages (Artículos)-----------
class PageVista(ListView):
    model= Article
    template_name="models/page.html"

class PageDetailView(DetailView):
    model=Article
    template_name="models/page_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PageCreateView(LoginRequiredMixin, TemplateView):
    template_name="forms/page_forms.html"
    def get(self, request, status=None):
        context={"form": ArticleForm()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= ArticleForm(request.POST, request.FILES)
      if miform.is_valid():
        info= miform.cleaned_data
        title=  info['title'] 
        subtitle=  info['subtitle'] 
        body=  info['body'] 
        author=  info['author'] 
        date=  info['date'] 
        image=  info['image']
        var_1 = Article(title=title, subtitle=subtitle, body=body, author=author, date=date, image=image)
        var_1.save()
        print(miform.errors)
        print("to gucci")
        # return render(request, self.template_name)
        return redirect('/page/')
      else:
          print(miform.errors)
          miform=ArticleForm()
          print("algo raro está pasando")
          
      context={'form':ArticleForm()}
      return render(request,self.template_name, context)


class PageUpdateView(LoginRequiredMixin,UpdateView):
    model=Article
    template_name= "update/page_update.html"
    success_url="/page/"
    fields=["title","subtitle", "body", "author", "date", "image"]

class PageDeleteView(LoginRequiredMixin,DeleteView):
    model=Article
    success_url="/page/"
    template_name="article_confirm_delete.html"


#-------- Sección de avatar-----------

class AddAvatarView(LoginRequiredMixin, TemplateView):
    template_name="forms/avatar_forms.html"
    def get(self, request, status=None):
        context={"form": AvatarForm()}
        return render(request, self.template_name, context)

    def post(self, request):   
      miform= AvatarForm(request.POST, request.FILES)
      if miform.is_valid():
        info= miform.cleaned_data
        image=  info['image']
        var_1 = Avatar(image=image, user=self.request.user)
        var_1.save()
        print("to gucci")
        # return render(request, self.template_name) este no
        return redirect('/accounts/profile')
      else:
          print(miform.errors)
          miform=AvatarForm()
          print("algo raro está pasando")
          
      context={'form':AvatarForm()}
      return render(request,self.template_name, context)

class UpdateAvatarView(LoginRequiredMixin, UpdateView):
    template_name="update/update_avatar.html"
    model=Avatar
    success_url= '/accounts/profile'
    fields=['image']

    def get_object(self):
        avatar, created= Avatar.objects.get_or_create(user=self.request.user)
        return avatar


#-------- Sección de forms primera entrega-----------
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
        # return render(request, self.template_name,)
      else:
          miform=Usuario_Formulario()
      context={'form':Usuario_Formulario()}
      return render(request,self.template_name, context)

class Creador_Vista_Forms_CreateUpdate(TemplateView):
    template_name= 'forms/creador_forms.html'
    def get(self, request, status=None, creador_id=None):
        creador=None

        if creador_id:
            creador= Creador.objects.get(id=creador_id)

        if creador:
            miform= Creador_Formulario(initial={"name":creador.name, 
                                                "lastname":creador.lastname,
                                                "nickname":creador.nickname, 
                                                "password":creador.password, 
                                                "email":creador.email, 
                                                "age":creador.age, 
                                                })
        else: 
            miform=Creador_Formulario()
        
        context={"form": miform}
        return render(request, self.template_name, context)

    def post(self, request, creador_id=None):   
      Creador.objects.update_or_create(id=creador_id, defaults={'name':request.POST['name'],
                                                                'lastname':request.POST['lastname'],
                                                                'nickname':request.POST['nickname'],
                                                                'password':request.POST['password'],
                                                                'email':request.POST['email'],
                                                                'age':request.POST['age'],
                                                                               })

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
        # return render(request, self.template_name)
      else:
          miform=Espectador_Formulario()
      context={'form':Espectador_Formulario()}
      return render(request,self.template_name, context)

#-------- Sección de eliminar de primera entrega-----------
class VistaBorrarCreador(TemplateView):
    template_name="models/creador.html"

    def get(self, request, creador_id):
        var_eliminate=Creador.objects.get(id=creador_id)
        var_eliminate.delete()
        var_1=Creador.objects.all()
        context={"Creadores": var_1}
        return render(request, self.template_name, context)


#-------- Sección de busqueda de primera entrega-----------
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




# Sección de LOGIN-LOGOUT-REGISTER

class LoginView(TemplateView):
    template_name="login/login.html"

    def get(self, request):
        context={"form": AuthenticationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
          user= request.POST.get("username")
          password=request.POST.get("password")
          user_auth= authenticate(username= user, password= password)

          if user_auth:
              login(request, user_auth)
              context= {"message_ok":f"Bienvenido {user}"}
              return render(request, self.template_name, context)
          
          else:
              context={"form": AuthenticationForm(),"message":"Usuario Invalido"}
              return render(request, self.template_name, context)

        else:
          context={"form": AuthenticationForm(),"message":"Formulario errado"}
          return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name="register/register.html"

    def get(self, request):
        # context={"form": UserCreationForm()}
        context={"form": UserRegisterForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        # form= UserCreationForm(request.POST)
        form= UserRegisterForm(request.POST)

        if form.is_valid():
          form.save()
          context={"form": UserRegisterForm(),"message_ok":"Usuario registrado correctamente"}
          return render(request, self.template_name, context)
          
        else:
          context={"form": UserRegisterForm(),"message_errors":"Ocurrió un error", "error":form.errors }
          print(form.errors)
          return render(request, self.template_name, context)


