from django.db import models

# Create your models here.
class my_model(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    auto_field = models.AutoField(primary_key=True)
    Big_int_field = models.BigIntegerField(default=0)
    binarY_fileld = models.BinaryField()
    charField = models.CharField(max_length=20)
    Today_date = models.DateField()
    Date_time = models.DateTimeField()
    duration = models.DurationField()
    file_path = models.FilePathField(path="model_app/upload/", match=".*\.(pdf|png)$")
    image_field = models.ImageField(upload_to='model_app/upload/')
    time_field = models.TimeField()
    
    
    
    def __str__(self):
        return self.name
    