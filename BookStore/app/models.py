from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    birthDate=models.DateField()
    biography=models.TextField()
    
class Book(models.Model):
    title=models.CharField(max_length=100)  
    author=models.ForeignKey(Author,on_delete=cas)  
