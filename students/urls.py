from django.urls import path
from . import views  # . means current path

# urlpatterns = [
#     path('', views.index, name='index'),  # Name the URL pattern as 'index'
#     path('about/', views.about, name='about'),  # Name the URL pattern as 'about'
#     # Additional URL patterns...
# ]

urlpatterns = [
    path("", views.index, name="index"),
    #  <int:id> is a path converter that allows us to create dynamic urls
    path("<int:id>", views.view_student, name="view_student"),
    path("add/", views.add, name="add"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name='delete'),
]
