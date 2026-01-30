from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(("name"), max_length=50)

    class Meta:
        abstract = True

class Student(Person):
    age = models.IntegerField(("age"))

class Doctor(Person):
    specialization = models.CharField(max_length=100)

class Patient(Person):
    disease = models.CharField(max_length=200)
