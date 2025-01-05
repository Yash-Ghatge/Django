
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.Auth,name='Auth'),
    path('<int:order_id>/',views.Details,name='Details')
]