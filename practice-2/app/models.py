from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books",null=True,blank=True)
    def __str__(self):
        return self.name
    
class Review(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    message = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message

class Category(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name