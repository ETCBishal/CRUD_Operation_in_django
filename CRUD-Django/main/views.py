from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.views import View


class Index(View):
    def get(self,request):
        students = Student.objects.all()
        return render(request,'index.html',{'students':students})

class AddStudents(View):
    def get(self,request):
        addStudentForm = StudentForm()
        return render(request,'add-students.html',{'form':addStudentForm})
    
    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

class EditStudents(View):
    def get(self,reqeust,id):
        student = Student.objects.get(id = id)
        form = StudentForm(instance=student)
        return render(reqeust,'edit-student.html',{'form':form})
    
    def post(self,reqeust,id):
        student = Student.objects.get(id = id)
        form = StudentForm(reqeust.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')

class DeleteStudents(View):
    def get(self,request,id):
        student = Student.objects.get(id = id)
        student.delete()
        return redirect('/') 
        

