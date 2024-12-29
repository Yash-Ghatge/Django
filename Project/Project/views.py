from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello! Your at HomePage")

def About(request):
    return HttpResponse("Hello! Your at About Page")

def Contact(request):
    return HttpResponse("Hello! Your at Contact Page")