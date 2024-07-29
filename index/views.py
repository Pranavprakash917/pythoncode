from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")

def index1(request):
    return render(request,'index.html')

def index2(request):
    person={
        'name':'pranav',
        'age':22,
        'place':'mavelikara'
    }
    return render(request,'variable.html',person)

def index3(request):
    classes={
        'name': 'praveen',
        'age' : 20,
        'place' : 'Alappuzha'
    }
    return render(request,'class.html',classes)

def index4(request):
    numbers = {
        'num1': [10, 100, 1000, 10000, 100000]
    }
    return render(request, 'numbers.html', numbers)

def index5(request):
    numbers = {
        'num2' : 10
    }
    return render(request,'index1.html',numbers)
