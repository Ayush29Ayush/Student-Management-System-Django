from django.contrib import admin
from .models import Student

# Register your models here.
#! admin.site.register(student) now knows that we want to use django admin to manipulate students and that it should display our students app and its database model student on the admin page in the django admin
admin.site.register(Student)