from django.db import models

# Create your models here.
class Servic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)

class kada(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets')

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(max_length=100000)




