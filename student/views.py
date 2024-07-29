from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import courses,fees
from django.contrib.auth import authenticate,login as auth_login
from django.conf import settings
from django.core.mail import send_mail
def insert(request):
    if request.method=='GET':
        return render(request,'insert.html')
    elif request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        course=request.POST['course']
        courses.objects.create(firstname=firstname, lastname=lastname, course= course)
        return HttpResponse("Value inserted successfully")


def insert1(request):
    if request.method=='GET':
        return render(request,'insert1.html')
    elif request.method == 'POST':
        student_name = request.POST['student_name']
        amount = request.POST['amount']
        fees.objects.create(student_name=student_name, amount=amount)
        return HttpResponse("Value inserted successfully")

def read(request):
    ob = courses.objects.all()
    return render(request,'read.html',{'ob':ob})

def update(request,id):
    if request.method=='GET':
        ob=courses.objects.get(id=id)
        return render(request,'update.html',{'ob':ob})
    elif request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        courses.objects.filter(id=id).update(firstname=firstname,lastname=lastname)
        return read(request)

def delete(request,id):
    courses.objects.get(id=id).delete()
    return read(request)

def create_user(request):
    if request.method=='GET':
        return render(request,'user.html')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
    User.objects.create_user(username=username,password=password)
    return HttpResponse("User created successfully")

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        a=request.POST['username']
        b=request.POST['password']
        value=authenticate(username=a,password=b)
        if value is not None:
            return HttpResponse("user login")
        else:
            return HttpResponse("invalid username or password")


def email(request):
    send_mail(
        "django project",
        "this is for text mail",
        settings.EMAIL_HOST_USER,
        ["anjuvenu21@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email Send")
