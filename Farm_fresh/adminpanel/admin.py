from django.contrib import admin
from .models import Product, Category, EmployeeAttendance, Employee, OrderPlaced, Payment,about_us,contact_us

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

admin.site.register(Category)
admin.site.register(EmployeeAttendance)
admin.site.register(Employee)

@admin.register(OrderPlaced)
class OrderplacedAdmin(admin.ModelAdmin):
    list_display = ['username', 'ordered_date', 'status', 'Shipping', 'order_updated_date']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['amount']








admin.site.register(about_us)
admin.site.register(contact_us)