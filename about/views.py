from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    return HttpResponse("Welcome World")

def about1(request):
    return render(request,'about.html')

# Create your views here.
