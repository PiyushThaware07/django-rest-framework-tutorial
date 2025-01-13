from django.db import models

# Create your models here.
class Instructor(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    instructor = models.ForeignKey(Instructor, related_name='courses', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name
    
class Department(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100,default="Unknown")
    def __str__(self):
        return self.name