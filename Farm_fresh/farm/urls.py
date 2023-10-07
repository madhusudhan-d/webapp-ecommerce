from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import PasswordChangeForm


urlpatterns = [
    path('', views.home, name='home'),
    path('p_list/<int:pk>',views.product_list, name='p_list'),
    path('p_details/<int:pk>', views.product_details, name='p_details'),
    path('login/', views.login, name='farm_login'),
    path('about/', views.about,name='about_us'),
    path('farm_contact/', views.contact,name='farm_contact'),
    path('customer_register/', views.customer_register,name='customer_register'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('check_out/', views.check_out, name='check_out'),
    path('orders/', views.orders, name='orders'),
    path('wish_list/', views.wish_list, name='add-to-wishlist'),
    path('order_status/', views.order_status, name='order_status'),
    path('profile/', views.profile,name='profile'),
    path('address/', views.address, name='address'),
    path('update_address/<int:pk>', views.updateAddress, name='update_address'),
    path('terms_conditions/', views.terms_condition, name='terms_conditions'),
    # path('change_password/', views.PasswordChangeView, name='change_password'),
    path('reset_confirm/<int:pk>', views.Reset_confirm_password, name='reset_confirm'),
    path('reset_password/', views.forgot_password_otp, name='reset_password'),
    path('email_otp/', views.email_otp, name='email_otp'),
    path('our_blog/', views.our_blog, name='our_blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('farm_complaint/', views.complaint, name='farm_complaint'),
    path('phone_otp/', views.phone_otp, name='phone_otp'),
    path('test/', views.test_1, name='test'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('change_password/',views.PasswordChangeView.as_view(template_name="farm_app/change_password.html"),
         name="change_password"),




    path('logout/', views.logout, name='logout'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)