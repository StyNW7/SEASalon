from django.urls import path
from . import views

# All urls in the website

urlpatterns = [
    path('', views.home, name='home'), #used as the index.html
    path('review2/', views.review, name='review2'),
    path('review/', views.add_review2, name='review'),
    path('customer/review/', views.dynamic_review, name='dynamic_review'), #used for customer to review
    path('reserve/', views.make_reservation, name='make_reservation'), #used for customer to reserve
    path('showreview/', views.show_reviews, name='show_reviews'), #used for admin to check review from customer
    path('addreview/', views.add_review, name='add_review'), 
    path('login/', views.login_view, name='login'), #used to login
    path('customer/history/', views.customer_dashboard, name='customer_history'), #used for customer to check their history
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'), #used for admin to create new branch and service
    path('customer/page/', views.customer_page, name='customer_page'), #used for customer dashboard
    path('page/', views.admin_page, name='page'),  # used for admin dashboard
    path('logout/', views.logout_view, name='logout'), #used to logout
    path('ajax/load-services/', views.load_services, name='ajax_load_services'),  # AJAX URL for dynamic_reserve for customer
    path('register/', views.register, name='register'), # used to register
]
