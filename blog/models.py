from django.db import models

# Create your models here.

class Usuario(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    nickname=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    email=models.EmailField()
    age=models.IntegerField()

class Creador(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    nickname=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    email=models.EmailField()
    age=models.IntegerField()

class Espectador(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=30, default="Sin nombre")
