from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Hotel(models.Model):
    menu =[
        ('P','Pizaa'),
        ('T','Tea'),
        ('C','Cake'),
        ('D','Dosa'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=menu)

    def __str__(self):
        return self.name
    

class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='hotelReview')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.TextField()
    date_add = models.DateTimeField(timezone.now)

    def __str__(self):
        return f'{self.user.username} review the {self.hotel.name}'
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    order = models.CharField(max_length=100)
    Bill = models.IntegerField()
    customer_opinion = models.ManyToManyField(Hotel,related_name='customers')

    def __str__(self):
        return f'{self.customer_name} have dinner in {self.customer_opinion.name}'

class Certificate(models.Model):
    certificate = models.OneToOneField(Hotel,on_delete=models.CASCADE,related_name='certificate')
    certificate_name = models.CharField(max_length=100)
    issued_date = models.DateTimeField(timezone.now)
    expired_date = models.DateTimeField(timezone.now)

    def __str__(self):
        return f'{self.certificate_name} is issued for {self.certificate.name}'