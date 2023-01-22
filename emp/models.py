from django.db import models


# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    

# this is for data send in browser

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    Testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/") 
    rating=models.IntegerField(max_length=1)  

        #  methodoverride
    def __str__(self) -> str:
            return self.Testimonial