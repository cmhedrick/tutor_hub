from django.db import models

# Create your models here.

class Tutor(models.Model):
    years = models.IntegerField()
    availability = models.DateField()
    name = models.CharField(max_length=35)
    picture = models.ImageField(upload_to='images/%Y/%m/%d')
    email = models.CharField(max_length=100)
    room = models.CharField(max_length=4)
    subject = models.CharField(max_length=35)
    phone = models.CharField(max_length=14)

class Student(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    visited = models.BooleanField()
    email = models.CharField(max_length=100)
    regular_teacher = models.CharField(max_length=35)
    session = models.CharField(max_length=35)
    grade = models.IntegerField()
    student_id = models.CharField(max_length=35)
    assignment = models.CharField(max_length=250)
