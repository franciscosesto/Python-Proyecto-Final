from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.

class Usuario(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    nickname=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return f" {self.name} {self.lastname} ({self.nickname})"

class Creador(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    nickname=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    email=models.EmailField()
    age=models.IntegerField()
    def __str__(self):
        return f" {self.name} {self.lastname} ({self.nickname})"

class Espectador(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=30, default="Sin nombre")
    def __str__(self):
        return f" {self.name}"

class Avatar(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to="avatars", null=True, blank=True)
    def __str__(self):
        return f"{self.user}"

class Article(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    body=RichTextField()
    author=models.CharField(max_length=50)
    date=models.DateTimeField(default=now)
    image= models.ImageField(upload_to="article", null=True, blank=True)
    def __str__(self):
        return f"{self.title}"

class ProfileData(models.Model):
    Descripción=RichTextField()
    Link=models.CharField(max_length=500)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}"

class Mensajes(models.Model):
    mensaje=models.CharField(max_length=2000)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"({self.user}) {self.mensaje}"