from django.db import models
from django.core.exceptions import ValidationError

# * validation
def validate_name(value):
    if not value.isalpha():
        raise ValidationError("Name should only contain alphabetic characters.")

def validate_password(value):
    if len(value) < 8 or len(value) > 18:
        raise ValidationError("Password must be between 8 and 18 characters.")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Password must contain at least one number.")
    if not any(char.isupper() for char in value):
        raise ValidationError("Password must contain at least one uppercase letter.")



# * models
class User(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    fname = models.CharField(max_length=50,validators=[validate_name])
    lname = models.CharField(max_length=50,validators=[validate_name])
    email = models.EmailField()
    password = models.CharField(max_length=18,validators=[validate_password])
    role = models.CharField(max_length=50,choices=[("guest","GUEST"),("admin","ADMIN")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.email
    
    
class Post(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts',null=True) # One-to-many relationship with User
    def __str__(self):
        return self.title