# Generated by Django 4.1.7 on 2023-06-22 11:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farm', '0003_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Action', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Published_At', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Published_By', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('category_image', models.ImageField(upload_to='product')),
                ('icon', models.ImageField(upload_to='product')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField()),
                ('Phone_Number', models.CharField(max_length=20)),
                ('Alternative_Phone_Number', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Action', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Category', models.TextField()),
                ('Product_Name', models.TextField()),
                ('Quantity', models.CharField(max_length=50)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Coupon_Code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.CharField(max_length=100)),
                ('Employee_name', models.CharField(max_length=100)),
                ('Phone_Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Designation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('Action', models.BooleanField(default=True)),
                ('employee_image', models.ImageField(upload_to='employee')),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Action', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terms_and_Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Action', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('composition', models.TextField()),
                ('product_image', models.ImageField(upload_to='product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.category')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.register')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateField()),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Processing', 'Processing'), ('Pending', 'Pending'), ('Cancel', 'Cancel')], default='pending', max_length=50)),
                ('Shipping', models.CharField(choices=[('Order Placed', 'Order Placed'), ('Packing', 'Packing'), ('Packed', 'Packed'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered')], default='Order Placed', max_length=50)),
                ('order_updated_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.profile')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpanel.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.register')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attended', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.register')),
            ],
        ),
    ]
