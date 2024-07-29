from django.shortcuts import render
from django.http import HttpResponse
def contact(request):
    return HttpResponse("Hello")

def contact1(request):
    return render(request,'contact.html')

# Create your views here.
