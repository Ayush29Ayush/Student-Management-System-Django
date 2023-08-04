from django.db import models


# Create your models here.
#! we are creating a new class called student that will be a model then inside this class we need to provide all of the students parameters like what properties does a student have that we might want to keep track off.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    #! any model can implement a double underscore str method which returns a string representation of that particular object
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"
