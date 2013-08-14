from django.db import models

# Create your models here.

class Tutor(models.Model):
    tutor_email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='images/%Y/%m/%d')

class Student(models.Model):
    student_id = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    grade = models.CharField(max_length=2)
    visited = models.BooleanField()
    email = models.CharField(max_length=100)
    regular_teacher = models.CharField(max_length=35)

class Session(models.Model):
    student_id = models.CharField(max_length=35)
    date = models.DateField()
    building = models.CharField(max_length=25)
    room = models.CharField(max_length=4)
    topic = models.CharField(max_length=25)
    assignments = models.CharField(max_length=100)

class Expertise(models.Model):
    tutor_email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Expertise"

class Availability(models.Model):
    tutor_email = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Availabilities"

class EmailAuth(models.Model):
    tutor_email = models.CharField(max_length=100)
