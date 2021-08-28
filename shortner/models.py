from django.db import models

# Create your models here.
# Url model for storing the input Url and its unique id 
class Url(models.Model): 
    inputUrl = models.CharField(max_length=13000)
    urlid = models.CharField(max_length=6)