from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    materials = models.TextField()

    def __str__(self):
        return self.name
