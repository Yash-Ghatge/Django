from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    #return HttpResponse("Hello! Your at HomePage")
    return render(request,'index.html')

def About(request):
    #return HttpResponse("Hello! Your at About Page")
    return render(request,'About.html')

def Contact(request):
    return HttpResponse("Hello! Your at Contact Page")