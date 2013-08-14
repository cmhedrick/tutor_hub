from django.db import models

# Create your models here.

APT_TIME = (
    ("B1", 'Block 1'),
    ("B2", 'Block 2'),
    ("B3", 'Block 3'),
    ("B4", 'Block 4'),
    ("A", 'A Lunch'),
    ("B", 'B Lunch'),
    ("C", 'C Lunch'),
    ("Eagle Time Workshop", 'Eagle TIme Workshop'),
    ("After School Thursday", 'After School Thursday'),
    ("Other: Special Workshop", 'Other: Special Workshop'),
    ("Other: After School", 'Other: After School')
)

GRADE = (
    ("9", 'Ninth Grade'),
    ("10", 'Tenth Grade'),
    ("11", 'Eleventh Grade'),
    ("12", 'Twelfth Grade')
)

VISITED = (
    ("Never.", 'Never.'),
    ("Yes, but not this school year.", 'Yes, but not this school year.'),
    ("Yes, I have been here already this school year.", 'Yes, I have been here already this school year.'),
)

REASON_VISITED = (
    ("It was teacher required.", 'It was teacher required.'),
    ("My teacher offered extra credit.", 'My teacher offered extra credit.'),
    ("I have been here before and found it useful.", 'I have been here before and found it useful.'),
    ("I heard about it and wanted to give it a try.", 'I heard about it and wanted to give it a try.'),
    ("I am rewriting and resubmitting an essay.", 'I am rewriting and resubmitting an essay.'),
)

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
    grade = models.CharField(max_length=2, choices=GRADE)
    email = models.CharField(max_length=100)
    teacher = models.CharField(max_length=35)

class Session(models.Model):
    student_id = models.CharField(max_length=35)
    date = models.DateField()
    building = models.CharField(max_length=25)
    room = models.CharField(max_length=4)
    topic = models.CharField(max_length=25)
    assignment = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=GRADE)  
    apt_time = models.CharField(max_length=25, choices=APT_TIME)
    reason_visited = models.CharField(max_length=50, choices=REASON_VISITED)
    visited = models.CharField(max_length=50, choices=VISITED)

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

class Email_Authentication(models.Model):
    tutor_email = models.CharField(max_length=100)
