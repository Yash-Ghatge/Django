from django.shortcuts import render

# Create your views here.
def Auth(request):
    return render(request,'Myapp/index.html')