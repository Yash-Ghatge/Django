from django.shortcuts import render
from .models import Hotel
from django.shortcuts import get_object_or_404
# Create your views here.
def Auth(request):
    orders = Hotel.objects.all()
    return render(request,'Myapp/index.html',{'orders':orders})

def Details(request,order_id):
    order = get_object_or_404(Hotel,pk=order_id)
    return render(request,'Myapp/all_index.html',{'order':order})

def Form_1(request):
    return render(request,'Myapp/Django_Form.html')