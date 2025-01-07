
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.Auth,name='Auth'),
    path('<int:order_id>/',views.Details,name='Details'),
    path('Form/',views.Form_1,name='Form')
]