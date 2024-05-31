from django.db import models

# Create your models here.
class my_class(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()