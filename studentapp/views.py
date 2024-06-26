from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def index(request):
    msg=""
    if request.method=="POST":
        student_id=request.POST['roll_no']
        student_name=request.POST['name']
        student_branch=request.POST['branch']
        student_email=request.POST['email']

        student = Student(roll_no=student_id, name=student_name,branch=student_branch,email=student_email)
        student.save()
        msg = "Registration Successfully Done"
    student_info = Student.objects.all()
    return render(request,"index.html",{"msg1":msg,'info':student_info})

def deletestudent(request,id):
    stud=Student.objects.get(roll_no=id)
    stud.delete()
    return redirect("index")

def updatestudent(request,id):
    stud=Student.objects.get(roll_no=id)
    return render(request,"update.html",{'s':stud})

def updatecode(request):
    if request.method=="POST":
        id=request.POST['roll_no']
        name=request.POST['name']
        branch=request.POST['branch']
        email=request.POST['email']

        Student.objects.filter(roll_no=id).update(roll_no=id,name=name,branch=branch,email=email)

    return redirect('index')    


