from django import forms

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
