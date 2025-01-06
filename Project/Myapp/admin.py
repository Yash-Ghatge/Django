from django.contrib import admin
from .models import Hotel,HotelReview,Customer,Certificate
# Register your models here.

class HotelReviewAdmin(admin.TabularInline):
    model = HotelReview
    extra = 2

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','date','type')
    inlines = [HotelReviewAdmin]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name','Bill','order')
    filter_horizontal = ('customer_opinion',)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name','issued_date')


admin.site.register(Hotel,HotelAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Certificate,CertificateAdmin)