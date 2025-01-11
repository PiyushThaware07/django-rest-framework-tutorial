from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    nationality = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.email



class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name




class Book(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    language = models.CharField(max_length=100,default="English")
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True)
    tags = models.ManyToManyField(Tag,related_name="books",blank=True,null=True)
    def __str__(self):
        return self.name
    
    
    
class Review(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.comment