from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):             
        return self.name
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)

