from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.TextField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    created_at=models.DateTimeField()
