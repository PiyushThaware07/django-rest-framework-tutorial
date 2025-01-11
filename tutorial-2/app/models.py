from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=50,choices=[("draft", "Draft"),("publish", "Publish")],default="draft")
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title