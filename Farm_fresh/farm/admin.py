from django.contrib import admin

from .models import Register,Profile,Complaints,Enquiry
# Register your models here.



@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'city', 'mobile', 'zipcode', 'state','town']


class registerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'confirm_password']


admin.site.register(Register, registerAdmin)


class complaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'subject', 'reason')

admin.site.register(Complaints,complaintAdmin)


class enquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(Enquiry,enquiryAdmin)














