from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_number",
            "first_name",
            "last_name",
            "email",
            "field_of_study",
            "gpa",
        ]
        labels = {
            "student_number": "Student Number",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "field_of_study": "Field of Study",
            "gpa": "GPA",
        }
        widgets = {
            "student_number": forms.NumberInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "field_of_study": forms.TextInput(attrs={"class": "form-control"}),
            "gpa": forms.NumberInput(attrs={"class": "form-control"}),
        }
# by default django doesn't add any css styling to the forms to make them look good however we can use the widget's attribute to solve this problem a widget is django's representation of an html input element the widget handles the rendering of the html and the extraction of data from a get or post dictionary that corresponds to the widget i want this student form to look good so i will style it using bootstrap i will add a bootstrap form-control class to each of the input fields this bootstrap class.