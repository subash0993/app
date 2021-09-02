from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm, FindStudent, DeleteStudent
from .models import StudentsList


def home(request):
    return render(request, 'navigation.html', {'title': 'Home'})


def display_students(request):
    if request.method == 'GET':
        students = StudentsList.objects.all()
        return render(request, 'display.html', {'students': students})


def add_students(request):
    form = StudentForm
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
            messages.success(request, 'Student data has been added')
            return redirect('/add')
    return render(request, 'form.html', {'form': form})


def get_student(request):
    form = FindStudent
    if request.method == 'POST':
        student = StudentsList.objects.filter(studentId=request.POST.get('studentId'))
        if student.count() == 1:
            student = StudentsList.objects.get(studentId=request.POST.get('studentId'))
            return render(request, 'display.html', {'students': [student]})
        else:
            messages.error(request, f"Student Id {request.POST.get('studentId')} not found")
            return redirect('/find')
    return render(request, 'find.html', {'form': form})


def delete_student(request):
    form = DeleteStudent
    if request.method == 'POST':
        student = StudentsList.objects.filter(studentId=request.POST.get('studentId'))
        if student.count() == 1:
            student.delete()
            messages.info(request, f"Student Id {request.POST.get('studentId')} deleted")
            return redirect('/delete')
        else:
            messages.error(request, f"Student Id {request.POST.get('studentId')} not found")
    return render(request, 'delete.html', {'form': form})
