from django.db import models
from django.utils import timezone
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