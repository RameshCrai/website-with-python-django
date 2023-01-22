from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=250)
    age=models.CharField(max_length=10)
    is_Active=models.BooleanField(default=False)
    mobile=models.IntegerField(max_length=10)


    



