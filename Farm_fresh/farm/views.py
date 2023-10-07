from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Register, Profile, Complaints, Enquiry
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
import random
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangingForm
from adminpanel.models import Product, Category, contact_us, about_us, Blog




def home(request):
    category = Category.objects.all()
    context = {'category': category}
    print('you are:', request.session.get('username'))
    return render(request, 'farm_app/home.html', context)



def product_list(request,pk):
    category = Category.objects.all()
    cat = Category.objects.get(id=pk)
    product = Product.objects.filter(category=cat)
    context = {
        'product': product,
        'category': category,

    }
    return render(request, 'farm_app/product_list.html', context)



def product_details(request,pk):

    product = Product.objects.get(id=pk)
    context = {
        'product': product,

    }
    return render(request, 'farm_app/product_details.html',context)


def about(request):
    category = Category.objects.all()
    about = about_us.objects.all()
    context = {'about': about, 'category': category}
    return render(request, 'farm_app/about.html', context)


def contact(request):
    category = Category.objects.all()
    contact1 = contact_us.objects.all()
    context = {'contact1': contact1, 'category': category}
    return render(request, 'farm_app/contact.html', context)

def login(request):
    if request.method == 'GET':
        return render(request, 'farm_app/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        reg = Register.get_customer_by_username(username)
        error_message = None
        if reg:
            flag = check_password(password, reg.password)

            if flag:
                request.session['reg_id'] = reg.id
                request.session['username'] = reg.username
                return redirect('home')
            else:
                error_message = 'username or password invalid..!!'


        else:
            error_message = 'username or password invalid..!!'

        print(reg)
        print(username,password)
        return render(request, 'farm_app/login.html', {'error': error_message})



def validateCustomer(reg):
    error_message = None;
    if (not reg.username):
        error_message = "username required...!"
    elif len(reg.username) < 4:
        error_message = 'username must be 4 char long or more'
    elif len(reg.email) < 5:
        error_message = 'email must be 5 char long or more'
    elif len(reg.password) < 5:
        error_message = 'Password must be 5 char long or more'
    elif reg.isExists():
        error_message = 'Email Address Already Registered...'

    return error_message

def registerUser(request):
    postData = request.POST
    username = postData.get('username')
    email = postData.get('email')
    password = postData.get('password')
    confirm_password = postData.get('confirm_password')
    # validation
    value = {
        'username': username,
        'email': email,

    }
    error_message = None

    reg = Register(username=username,
                   email=email,
                   password=password,
                   confirm_password=confirm_password,
                   otp=Rotp,)

    error_message = validateCustomer(reg)

    # saving
    if not error_message:
        print(username, email, password, confirm_password)
        reg.password = make_password(reg.password)
        reg.register()
        return redirect('farm_login')
    else:
        data = {
            'error': error_message,
            'value': value

        }
        return render(request, 'farm_app/customer_register.html', data)

Rotp = random.randint(111111,999999)
def customer_register(request):
    if request.method == 'GET':
        return render(request, 'farm_app/customer_register.html')
    else:
        return registerUser(request)

def logout(request):
    request.session.clear()
    return redirect('farm_login')



def updateAddress(request, pk):
    pro = Profile.objects.get(id=pk)


    if request.method == 'POST':


        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        town = request.POST.get('town')
        zipcode = request.POST.get('zipcode')
        data = Profile(id=pk, name=name,mobile=mobile,address=address,state=state,city=city,town=town,zipcode=zipcode)
        data.save()
        return redirect('address')
    context = {'pro': pro}

    return render(request, 'farm_app/updateAddress.html',context)






def check_out(request):
    return render(request,"farm_app/check_out.html")


def add_cart(request):
    return render(request, 'farm_app/add_cart.html')


def orders(request):
    return render(request,"farm_app/orders.html")


def wish_list(request):
    return render(request,"farm_app/wish_list.html")


def order_status(request):
    return render(request,"farm_app/order_status.html")


def profile(request):
    pro = Register.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        town = request.POST.get('town')
        zipcode = request.POST.get('zipcode')
        data = Profile(name=name,mobile=mobile,address=address,state=state,city=city,town=town,zipcode=zipcode)
        data.save()

    context = {'pro': pro}
    return render(request, 'farm_app/profile.html', context)




def address(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile,
    }
    return render(request, 'farm_app/address.html', context)




def terms_condition(request):
    return render(request,"farm_app/terms_conditions.html")

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'change_password'
    success_url = reverse_lazy('farm_login')


def Reset_confirm_password(request,pk):
    password =  Register.objects.get(id=pk)
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password.password != password1:
            if password1 == password2:
                password.password = password1
                password.confirm_password = password.password
                password.save()
                return redirect('farm_login')
            else:
                form_url = reverse('reset_confirm', args=[password.id])
                return redirect(form_url)
    return render(request, 'farm_app/password_reset_confirm.html')


def forgot_password_otp(request):
    if request.method == 'POST':
        FP_otp = random.randint(111111, 999999)
        email = request.POST.get('email')
        cr =  Register.objects.get(email=email)
        cr.otp = FP_otp
        cr.save()
        send_mail('Forget Password',

                  f'''Dear USER,

                    We hope this email finds you well!

                    Your OTP is {FP_otp}

                ''',

                  'vandanamatta666@gmail.com',

                  [f'{email}', 'akulaniharika333@gmail.com'],

                  fail_silently=False)
        return redirect('email_otp')

    return render(request, 'farm_app/password_reset.html')


def email_otp(request):
    if request.method == 'POST':
        Otp = request.POST.get('number')
        try:
            o = Register.objects.get(otp=Otp)
            form_url = reverse('reset_confirm', args=[o.id])
            return redirect(form_url)
        except  Register.DoesNotExist:
            return redirect('email_otp')
    return render(request, 'farm_app/email_otp.html')


def our_blog(request):
    blog1 = Blog.objects.all()
    context = {
        'blog1': blog1
    }
    return render(request, 'farm_app/blog_details.html', context)


def blog_detail(request):
    return render(request, 'farm_app/blog_details.html')


def complaint(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        reason = request.POST.get('reason')
        data = Complaints(
            name=name,
            email=email,
            mobile=mobile,
            subject=subject,
            reason=reason,

        )
        data.save()

    return render(request, 'farm_app/complaint.html')


def phone_otp(request):
    return render(request, 'farm_app/number_otp.html')



def test_1(request):
    return render(request, 'farm_app/test.html')



def enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.Post.get('message')

        data = Enquiry(
            name=name,
            email=email,
            message=message,


        )
        data.save()

    return render(request, 'farm_app/contact.html')



