from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField
from django.forms import DateTimeInput, TextInput

class Usuario_Formulario(forms.Form):
    name=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    nickname=forms.CharField(max_length=15)
    password=forms.CharField(max_length=15)
    email=forms.EmailField()
    age=forms.IntegerField()

class Creador_Formulario(forms.Form):
    name=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    nickname=forms.CharField(max_length=15)
    password=forms.CharField(max_length=15)
    email=forms.EmailField()
    age=forms.IntegerField()

class Espectador_Formulario(forms.Form):
    age=forms.IntegerField()
    name=forms.CharField(max_length=30)


class UserRegisterForm(UserCreationForm):
      first_name=forms.CharField(label="Nombre")
      last_name=forms.CharField(label="Apellido")
      email= forms.EmailField()
      password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput, help_text="Debe contener más de 8 caracteres")
      password2= forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
      
     
      class Meta:
          model=User
          fields= ["first_name","last_name","username", "email", "password1", "password2"]
        #   Saca los mensajes de ayuda
          help_texts= {k:"" for k in fields}

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ArticleForm(forms.Form):
    title=forms.CharField(max_length=100, widget= TextInput())
    subtitle=forms.CharField(max_length=100)
    body=RichTextFormField()
    author=forms.CharField(max_length=50)
    date=forms.DateTimeField(widget= DateTimeInput(attrs={'class': 'form-control'}))
    image= forms.ImageField( )

class AvatarForm(forms.Form):
    image= forms.ImageField()


class ProfileDataForm(forms.Form):
    Descripción=RichTextFormField()
    Link=forms.CharField(max_length=500)

class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        
class MensajesForm(forms.Form):
    mensaje=forms.CharField(max_length=2000)
    
  
 
