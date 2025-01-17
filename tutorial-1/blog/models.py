from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title