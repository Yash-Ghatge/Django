from django.shortcuts import render
from .models import Hotel
# Create your views here.
def Auth(request):
    orders = Hotel.objects.all()
    return render(request,'Myapp/index.html',{'orders':orders})