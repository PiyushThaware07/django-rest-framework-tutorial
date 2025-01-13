from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in weeks",default=0)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)
    def __str__(self):
        return self.email
