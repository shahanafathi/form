from django.db import models

# Create your models here.
class regiter(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname
    
class rstr(models.Model):
    schlname=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phoneno=models.IntegerField()
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.schlname
   