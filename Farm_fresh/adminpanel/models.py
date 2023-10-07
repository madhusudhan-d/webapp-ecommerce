from datetime import datetime

from django.db import models
from farm.models import Register,Profile,Complaints
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    category_image = models.ImageField(upload_to='product', null=False, blank=False)
    icon = models.ImageField(upload_to='product', null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=100, unique=True)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    composition = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product', null=False, blank=False)

    def __str__(self):
        return self.title


class Employee(models.Model):
    Employee_id = models.CharField(max_length=100, null=False, blank=False)
    Employee_name = models.CharField(max_length=100, null=False, blank=False)
    Phone_Number = models.IntegerField()
    Email = models.EmailField(unique=True)
    Designation = models.CharField(max_length=50, null=False, blank=False)
    department = models.CharField(max_length=50, null=False, blank=False)
    Action = models.BooleanField(default=True)
    employee_image = models.ImageField(upload_to='employee', null=False, blank=False)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.Employee_id

class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)



class Cart(models.Model):
    username = models.ForeignKey(Register, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



STATE_CHOICES = (
   ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
   ("Andhra Pradesh", "Andhra Pradesh"),
   ("Arunachal Pradesh", "Arunachal Pradesh"),
   ("Assam", "Assam"),
   ("Bihar", "Bihar"),
   ("Chhattisgarh", "Chhattisgarh"),
   ("Chandigarh", "Chandigarh"),
   ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
   ("Daman and Diu", "Daman and Diu"),
   ("Delhi", "Delhi"),
   ("Goa", "Goa"),
   ("Gujarat", "Gujarat"),
   ("Haryana", "Haryana"),
   ("Himachal Pradesh", "Himachal Pradesh"),
   ("Jammu and Kashmir", "Jammu and Kashmir"),
   ("Jharkhand", "Jharkhand"),
   ("Karnataka", "Karnataka"),
   ("Kerala", "Kerala"),
   ("Ladakh", "Ladakh"),
   ("Lakshadweep", "Lakshadweep"),
   ("Madhya Pradesh", "Madhya Pradesh"),
   ("Maharashtra", "Maharashtra"),
   ("Manipur", "Manipur"),
   ("Meghalaya", "Meghalaya"),
   ("Mizoram", "Mizoram"),
   ("Nagaland", "Nagaland"),
   ("Odisha", "Odisha"),
   ("Punjab", "Punjab"),
   ("Pondicherry", "Pondicherry"),
   ("Rajasthan", "Rajasthan"),
   ("Sikkim", "Sikkim"),
   ("Tamil Nadu", "Tamil Nadu"),
   ("Telangana", "Telangana"),
   ("Tripura", "Tripura"),
   ("Uttar Pradesh", "Uttar Pradesh"),
   ("Uttarakhand", "Uttarakhand"),
   ("West Bengal", "West Bengal")
)





class Payment(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Processing', 'Processing'),
    ('Pending', 'Pending'),
    ('Cancel', 'Cancel'),
)
SHIPPING_CHOICES = (
    ('Order Placed', 'Order Placed'),
    ('Packing', 'Packing'),
    ('Packed', 'Packed'),
    ('Shipping', 'Shipping'),
    ('Delivered', 'Delivered'),
)


class OrderPlaced(models.Model):

    username = models.ForeignKey(Register, on_delete=models.CASCADE)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    Shipping = models.CharField(max_length=50, choices=SHIPPING_CHOICES, default='Order Placed')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    order_updated_date = models.DateField()


class about_us(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Action = models.BooleanField(default=True)

    def __self__(self):
        return self.Title

class contact_us(models.Model):
    Address = models.TextField()
    Phone_Number = models.CharField(max_length=20, null=False, blank=False)
    Alternative_Phone_Number = models.CharField(max_length=20)
    Email = models.EmailField()
    Action = models.BooleanField(default=True)






class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Published_At = models.DateTimeField(default=datetime.now, blank=True)
    Published_By = models.CharField(max_length=50)

    def __self__(self):
        return self.Title


class Terms_and_Conditions(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Action = models.BooleanField(default=True)

    def __self__(self):
        return self.Name


class FAQ(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Action = models.BooleanField(default=True)

    def __self__(self):
        return self.Name


class Coupon(models.Model):
    Product_Category = models.TextField()
    Product_Name = models.TextField()
    Quantity = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Coupon_Code = models.CharField(max_length=50)


