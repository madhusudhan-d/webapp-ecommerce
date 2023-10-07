
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('category/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_category/<int:pk>', views.Deletecategory, name='delete_category'),
    path('recover_password/', views.recover_password, name='recover_password'),
    path('add_product/', views.add_product, name='add_product'),
    path('orderlist/', views.orderList, name='orderlist'),
    path('updateorderlist/', views.updateorderList, name='updateorderlist'),
    path('update/<int:pk>', views.Update, name='update'),
    path('attendance/<int:pk>', views.calculate_attendance, name='attendance'),
    path('deleteemployee/<int:pk>', views.deleteemployee, name='deleteemployee'),

    path('add_employee', views.add_employee, name='add_employee'),
    path('confirmorders/', views.confirmOrders, name='confirmorders'),
    path('updateconfirm/', views.updateConfirm, name='updateconfirm'),

    path('processingorders/', views.processingOrders, name='processingorders'),
    path('updateprocessing/', views.updateProcessing, name='updateprocessing'),

    path('pendingorders/', views.pendingOrders, name='pendingorders'),
    path('updatepending/', views.updatePending, name='updatepending'),

    path('cancelorders/', views.cancelOrders, name='cancelorders'),
    path('updatecancel/', views.updateCancel, name='updatecancel'),

    # path('faq/', views.faq, name='faq'),
    # path('enquiry/', views.enquiry, name='enquiry'),
    # path('terms_and_conditions/', views.terms,name='terms_and_conditions'),
    # path('about/', views.about,name='about'),
    # path('blog/', views.blog, name='blog'),
    # path('contact_us/', views.contact, name='contact_us'),
    path('coupon/', views.coupon, name='coupon'),
    path('terms_and_conditions/', views.add_terms, name='terms_and_conditions'),
    path('about/', views.add_about, name='about'),
    # path('blog', views.add_blog, name='blog'),
    path('contact/', views.add_contact, name='contact'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('faq/', views.add_faq, name='faq'),
    path('contact2/<int:pk>', views.updatecontact, name='contact2'),
    path('about2/<int:pk>', views.updateabout, name='about2'),
    path('terms2/<int:pk>', views.updateterms, name='terms2'),
    path('faq2/<int:pk>', views.updatefaq, name='faq2'),
    path('deletecontact/<int:pk>', views.deletecontact, name='deletecontact'),
    path('deleteenquiry/<int:pk>/', views.deleteenquiry, name='deleteenquiry'),
    path('deleteabout/<int:pk>/', views.deleteabout, name='deleteabout'),
    path('deletefaq/<int:pk>/', views.deletefaq, name='deletefaq'),
    path('deleteterms/<int:pk>/', views.deleteterms, name='deleteterms'),


    path('active/', views.Active_customer, name='active'),
    path('deactive_customer/', views.deactive_customer, name='deactive_customer'),
    path('recntly_addedcustomer/', views.recently_addedcustomer, name='recntly_addedcustomer'),
    path('spam_customer/', views.spam_customer, name='spam_customer'),
    path('order_tracking/', views.order_tracking, name='order_tracking'),
    path('recently_added_customers/', views.recently_added_customers, name='recently_added_customers'),
    path('complaints/', views.complaints, name='complaints'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

