from django.shortcuts import render
from .models import Student

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StudentForm


# Create your views here.
#! request parameter here represents the http request to access the data from the server
#! {"students": Student.objects.all()}, here we are fetching all the object data from the student class and naming that output as 'students'
def index(request):
    return render(request, "students/index.html", {"students": Student.objects.all()})


#! Action to view the details of the selected student

# The reverse function takes the view name as an argument (in this case, 'my-view') and returns the corresponding URL for that view. The benefit of using reverse is that it allows you to avoid hardcoding URLs in your code, making it easier to maintain your project.


# pk = id this means get me the student whose primary key in the database is equal to the id passed as an argument to this function. Using pk as shown here is django's generic way of referencing the primary key
def view_student(request, id):
    student = Student.objects.get(pk=id)
    # path('', views.index, name='index'),  # Name the URL pattern as 'index'. Check urls.py file from students folder
    # the reverse function allows us to avoid hard coding a url in our view it takes the name of a particular view and gets us what the url is.
    return HttpResponseRedirect(reverse("index"))


def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data["student_number"]
            new_first_name = form.cleaned_data["first_name"]
            new_last_name = form.cleaned_data["last_name"]
            new_email = form.cleaned_data["email"]
            new_field_of_study = form.cleaned_data["field_of_study"]
            new_gpa = form.cleaned_data["gpa"]

            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa,
            )
            new_student.save()
            return render(
                request, "students/add.html", {"form": StudentForm(), "success": True}
            )
    else:
        form = StudentForm()
    return render(request, "students/add.html", {"form": StudentForm()})


def edit(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(
                request, "students/edit.html", {"form": form, "success": True}
            )
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, "students/edit.html", {"form": form})


def delete(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse("index"))
