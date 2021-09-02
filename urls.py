from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display', views.display_students, name='displaystudents'),
    path('add', views.add_students, name='addstudent'),
    path('find', views.get_student, name='getstudent'),
    path('delete', views.delete_student, name='deletestudent'),
]
