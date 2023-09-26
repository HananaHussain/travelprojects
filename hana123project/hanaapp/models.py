from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Person(models.Model):
    imgs=models.ImageField(upload_to='pics')
    hd=models.CharField(max_length=250)
    para=models.TextField()

    def __str__(self):
        return self.namej
        return self.hd


