from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    def my_property(self):
        return self.name + ' ' + self.surname
    my_property.short_description = "Full name"

    full_name = property(my_property)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)

