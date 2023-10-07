from datetime import datetime

from django.shortcuts import render, redirect
from .models import Category, Product, Employee, EmployeeAttendance, about_us, contact_us, Terms_and_Conditions, FAQ,  OrderPlaced
from .forms import ProductForm, CategoryForm
from django.core.mail import send_mail
import random
import string
from farm.models import Register,Profile,Complaints,Enquiry

def login(request):


    return render(request, 'adminpanel/login.html')


def recover_password(request):
    return render(request, 'adminpanel/recover_password.html')


# def add_product(request):
#     return render(request, 'adminpanel/add_product.html')


def dashboard(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'adminpanel/dashboard.html', context)


# def category(request):
#     return render(request, 'adminpanel/category.html')


def orderList(request):
    orders = OrderPlaced.objects.all()

    context = {
        'orders': orders,
    }
    return render(request, 'adminpanel/orderlist.html', context)


def updateorderList(request, pk):
    orders = OrderPlaced.objects.get(id=pk)
    order = OrderPlaced.objects.all()
    customer = Profile.objects.all()
    username = Register.objects.all()

    if request.method == 'POST':

        pk = request.POST.get('order_id')
        ordered_date = request.POST.get('ORD')
        Shipping = request.POST.get('shipping_status')
        status = request.POST.get('order_status')
        comment_box = request.POST.get('comments')

        update = OrderPlaced(

            id=pk,
            ordered_date=ordered_date,
            # payment_status=payment,
            Shipping=Shipping,
            status=status,
            comment_box=comment_box,
        )

        update.save()
        return redirect('orderlist')

    context = {
        'orders': orders,
        'order': order,
        # 'product': product,
        # 'category': category,
        'customer': customer,
        # 'payment': payment,
        'username': username,
    }
    return render(request, 'adminpanel/updateorderlist.html', context)

def addemployee(request):
    return render(request, 'adminpanel/add_employee.html')


def confirmOrders(request):
    return render(request, 'adminpanel/confirmorders.html')


def updateConfirm(request):
    return render(request, 'adminpanel/updateconfirmorders.html')


def processingOrders(request):
    return render(request, 'adminpanel/processingorders.html')


def updateProcessing(request):
    return render(request, 'adminpanel/updateprocessingorders.html')


def pendingOrders(request):
    return render(request, 'adminpanel/pendingorders.html')


def updatePending(request):
    return render(request, 'adminpanel/updatependingorders.html')


def cancelOrders(request):
    return render(request, 'adminpanel/cancelorders.html')


def updateCancel(request):
    return render(request, 'adminpanel/updatecancelorders.html')




def enquiry(request):
    enquiry1 = Enquiry.objects.all()
    context = {'enquiry1': enquiry1}
    return render(request, 'adminpanel/enquiry.html', context)

def Active_customer(request):
    # rpassword = random.randint(11111, 99999)
    date = datetime.now()
    cust = Profile.objects.all()
    if request.method == "POST":
        username = request.POST.get('user_name')
        mobile = request.POST.get('mobile')
        # Address = request.POST.get('address')
        # # Country = request.POST.get('Country')
        # state = request.POST.get('state')
        # city = request.POST.get('city')

        # zipcode = request.POST.get('zip')
        email = request.POST.get('email')
        password = generate_password()
        Confirm_password = password
        data = Register(username=username, email=email, password=password, confirm_password=Confirm_password)
        data.save()
        # Send email to the employee
        subject = 'Welcome to the company!'
        message = f'Hello {data.username},\n\nYour account has been created with the following details:\n\nName: {data.username}\nPassword: {data.password}'
        from_email = 'vandanamatta666@gmail.com'
        recipient_list = [data.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect('Active')

    context = {'cust': cust}
    return render(request, 'adminpanel/active_customer_table.html', context)


def deactive_customer(request):
    return render(request, 'adminpanel/deactive_customer.html')


def recently_addedcustomer(request):
    return render(request, 'adminpanel/recently_addedcustomer.html')


def spam_customer(request):
    return render(request, 'adminpanel/spam_customer.html')

def order_tracking(request):
    return render(request, 'adminpanel/order_tracking.html')

def recently_added_customers(request):
    return render(request, 'adminpanel/recently_added_customers.html')

def employeeprofile(request):
    return render(request, 'adminpanel/Employee_profile.html')

def complaints(request):
    complaints = Complaints.objects.all()
    context = {'complaints': complaints}
    return render(request, 'adminpanel/complaints.html', context)


def add_category(request):
    context = None
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            icon = form.cleaned_data['icon']
            c = Category(name=name, icon=icon)
            c.save()
            form = CategoryForm()  # Create a new instance of the form
    else:
        cate = Category.objects.all()
        form = CategoryForm()
        context = {'cate': cate,
                   'form': form}
    return render(request, 'adminpanel/category.html', context)

def Deletecategory(request, pk):
    cat = Category.objects.get(id=pk)
    cat.delete()

    return redirect('add_category')

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            selling_price = form.cleaned_data['selling_price']
            discounted_price = form.cleaned_data['discounted_price']
            description = form.cleaned_data['description']
            composition = form.cleaned_data['composition']
            category = form.cleaned_data['category']
            product_image = form.cleaned_data['product_image']
            reg = Product(title=title, selling_price=selling_price, discounted_price=discounted_price, description=description, composition=composition, category=category, product_image=product_image)
            reg.save()
            form = ProductForm()  # Create a new instance of the form
    else:
        form = ProductForm()  # Create a new instance of the form
    context = {'form': form}
    return render(request, 'adminpanel/add_product.html', context)








def deleteemployee(request, pk):
    D = Employee.objects.get(id=pk)
    D.delete()
    # return redirect('employee')
    return render(request, 'adminpanel/add_employee.html')

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def add_employee(request):
    empl = Employee.objects.all()
    if request.method == "POST":
        Employee_id = request.POST['Employee_id']
        Employee_name = request.POST['Employee_name']
        Phone_Number = request.POST['Phone_Number']
        Email = request.POST['Email']
        Designation = request.POST['Designation']
        department = request.POST['department']
        password = generate_password()
        data = Employee(Employee_id=Employee_id, Employee_name=Employee_name, Phone_Number=Phone_Number, Email=Email,
                        Designation=Designation, department=department, password=password)
        data.save()

        # Send email to the employee
        subject = 'Welcome to the company!'
        message = f'Hello {data.Employee_name},\n\nYour account has been created with the following details:\n\nName: {data.Employee_name}\nPassword: {data.password}'
        from_email = 'damireddim@gmail.com'
        recipient_list = [data.Email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('add_employee')
    context = {'empl': empl}
    return render(request, 'adminpanel/add_employee.html', context)



def calculate_attendance(request, pk):
    employee = Employee.objects.get(id=pk)
    attendance_records = EmployeeAttendance.objects.filter(employee=employee)
    total_working_days = attendance_records.count()
    days_present = attendance_records.filter(attended=True).count()
    days_absent = total_working_days - days_present

    if total_working_days > 0:
        attendance_percentage = (days_present / total_working_days) * 100
    else:
        attendance_percentage = 0

    context = {
        'employee': employee,
        'attendance_percentage': attendance_percentage,
        'total_working_days': total_working_days,
        'days_present': days_present,
        'days_absent': days_absent,
    }

    return render(request, 'adminpanel/employee_profile.html', context)

def Update(request, pk):
    update = Employee.objects.get(id=pk)

    if request.method == 'POST':
        Employee_id = request.POST.get('Employee_id')
        Employee_name = request.POST.get('Employee_name')
        Phone_Number = request.POST.get('Phone_Number')
        Email = request.POST.get('Email')
        Designation = request.POST.get('Designation')
        department = request.POST.get('department')

        employ = Employee(
             id=pk,
             Employee_id=Employee_id,
             Employee_name=Employee_name,
             Phone_Number=Phone_Number,
             Email=Email,
             Designation=Designation,
             department=department

        )
        employ.save()
        return redirect('add_employee')
    context = {'update': update}

    return render(request, 'adminpanel/update_employee.html', context)


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             login_obj = Employee.objects.get(username=username)
#             if login_obj.password == password:
#                 # Authentication successful
#                 request.session['username'] = username
#                 return redirect('dashboard')  # Redirect to the dashboard page after successful login
#             else:
#                 error_message = 'Invalid username or password.'
#         except Employee.DoesNotExist:
#             error_message = 'Invalid username or password.'
#     else:
#         error_message = None
#
#     return render(request, 'login.html', {'error_message': error_message})



def updateabout(request, pk):
    about = about_us.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        data = about_us(id=pk, Title=title, Description=description)
        data.save()
        return redirect('about')

    context = {'about': about}

    return render(request, 'adminpanel/update_about.html', context)

def updateterms(request, pk):
    terms = Terms_and_Conditions.objects.get(id=pk)

    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        data = Terms_and_Conditions(id=pk, Name=Name, Email=Email)
        data.save()
        return redirect('terms_and_conditions')

    context = {'terms': terms}

    return render(request, 'adminpanel/update_terms.html', context)


def updatefaq(request, pk):
    faq = FAQ.objects.get(id=pk)

    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        data = FAQ(id=pk, Name=Name, Email=Email)
        data.save()
        return redirect('terms_and_conditions')

    context = {'faq': faq}

    return render(request, 'adminpanel/updatefaq.html', context)


def updatecontact(request, pk):
    contact = contact_us.objects.get(id=pk)

    if request.method == "POST":
        address = request.POST.get('address')
        phone_Number = request.POST.get('phone_Number')
        alternative_Phone_Number = request.POST.get('alternative_Phone_Number')
        email = request.POST.get('email')
        data = contact_us(id=pk, Address=address, Phone_Number=phone_Number, Alternative_Phone_Number=alternative_Phone_Number,
                          Email=email)
        data.save()
        return redirect('contact')

    context = {'contact': contact}

    return render(request, 'adminpanel/edit_contact.html', context)

def add_about(request):
    about1 = about_us.objects.all()
    if request.method == "POST":
        Title = request.POST['Title']
        Description = request.POST['Description']
        data = about_us(Title=Title, Description=Description)
        data.save()
        return redirect('about')
    context = {'about1': about1}
    return render(request, 'adminpanel/about.html', context)


def add_contact(request):
    contact1 = contact_us.objects.all()
    if request.method == "POST":
        Address = request.POST.get('Address')
        Phone_Number = request.POST.get('Phone_Number')
        Alternative_Phone_Number = request.POST.get('Alternative_Phone_Number')
        Email = request.POST.get('Email')
        data = contact_us(Address=Address, Phone_Number=Phone_Number, Alternative_Phone_Number=Alternative_Phone_Number,
                          Email=Email)
        data.save()
        return redirect('contact')
    context = {'contact1': contact1}
    return render(request, 'adminpanel/contact_us.html', context)

def add_faq(request):
    faq1 = FAQ.objects.all()
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        data = FAQ(Name=Name, Email=Email)
        data.save()
        return redirect('faq')
    context = {'faq1': faq1}
    return render(request, 'adminpanel/faq.html', context)

def add_terms(request):
    tc1 = Terms_and_Conditions.objects.all()
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        data = Terms_and_Conditions(Name=Name,
                                    Email=Email)
        data.save()
        return redirect('terms_and_conditions')
    context = {'tc1': tc1}
    return render(request, 'adminpanel/terms and conditions.html', context)



def deletecontact(request, pk):
    c1 = contact_us.objects.get(id=pk)
    c1.delete()
    return redirect('contact')


def deleteenquiry(request, pk):
    e1 = Enquiry.objects.get(id=pk)
    e1.delete()
    return redirect('enquiry')


def deleteabout(request, pk):
    a1 = about_us.objects.get(id=pk)
    a1.delete()
    return redirect('about')


def deletefaq(request, pk):
    f1 = FAQ.objects.get(id=pk)
    f1.delete()
    return redirect('faq')


def deleteterms(request, pk):
    t1 = Terms_and_Conditions.objects.get(id=pk)
    t1.delete()
    return redirect('terms_and_conditions')

def coupon(request):
    return render(request, 'adminpanel/coupon.html')