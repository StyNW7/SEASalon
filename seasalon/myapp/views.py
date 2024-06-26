# Library Import

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Branch, Service
from .forms import BranchForm, ServiceForm

from .forms import ReviewForm
from .models import Review

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


# Validation


def customer_required(user):
    return user.is_authenticated and user.role == 'customer'

def admin_required(user):
    return user.is_authenticated and user.role == 'admin'

# Home Page

def home(request):
    return render(request, 'index.html')


# Admin Page

@login_required(login_url='/login/')
@user_passes_test(admin_required, login_url='/login/')
def admin_page(request):
    return render(request, 'admin_page.html')


# Customer Page

@login_required(login_url='/login/')
@user_passes_test(customer_required, login_url='/login/')
def customer_page(request):
    return render(request, 'customer_page.html')


# Admin to create new branch and new service


@login_required(login_url='/login/')
@user_passes_test(admin_required, login_url='/login/')
def admin_dashboard(request):
    branches = Branch.objects.all()
    services = Service.objects.all()
    branch_form = BranchForm()
    service_form = ServiceForm()

    if request.method == 'POST':
        if 'branch_form' in request.POST:
            branch_form = BranchForm(request.POST)
            if branch_form.is_valid():
                branch_form.save()
                return redirect('admin_dashboard')
        elif 'service_form' in request.POST:
            service_form = ServiceForm(request.POST)
            if service_form.is_valid():
                service_form.save()
                return redirect('admin_dashboard')

    context = {
        'branches': branches,
        'services': services,
        'branch_form': branch_form,
        'service_form': service_form,
    }

    return render(request, 'admin_dashboard.html', context)


# Admin to check review from customer


@login_required(login_url='/login/')
@user_passes_test(admin_required, login_url='/login/')
def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


# Dyanmic Review Page (Used)


@login_required(login_url='/login/')
@user_passes_test(customer_required, login_url='/login/')
def dynamic_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer_name = request.user.username  # Set customer name to logged-in user's username
            review.save()
            return redirect('dynamic_review')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'customer_review.html', {'form': form, 'reviews': reviews})


# Customer Dashboard


@login_required(login_url='/login/')
@user_passes_test(customer_required, login_url='/login/')
def customer_dashboard(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-reservation_time')
    return render(request, 'customer_dashboard.html', {'reservations': reservations})


# Reservation Page


from .models import Reservation, Branch, Service
from .forms import ReservationForm

from django.http import JsonResponse
from django.core.exceptions import ValidationError

@login_required(login_url='/login/')
def load_services(request):
    branch_id = request.GET.get('branch_id')
    services = Service.objects.filter(branch_id=branch_id).order_by('name')
    return JsonResponse(list(services.values('id', 'name')), safe=False)

@login_required(login_url='/login/')
@user_passes_test(customer_required, login_url='/login/')
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Reservation made successfully!")
            return redirect('customer_history')
        else:
            messages.error(request, "There was an error with your reservation. Please check the form and try again.")
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})


# Register Page


from .forms import CustomRoleCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomRoleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRoleCreationForm()
    return render(request, 'register.html', {'form': form})


# Login Page


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'customer':
                return redirect('customer_page')
            elif user.role == 'admin':
                return redirect('page')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# Log out


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')


# Not use


# Review Page (Archieved)


@login_required(login_url='/login/')
@user_passes_test(customer_required, login_url='/login/')
def add_review2(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'dynamic_review.html', {'form': form})


# Review Page

def review(request):
    return render(request, 'review.html')

# Add Review Page

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Ganti dengan URL sukses menyimpan ulasan
    else:
        form = ReviewForm()
    
    return render(request, 'review_form.html', {'form': form})


# Reservation Page Archieved


# from .forms import ReservationForm

# def make_reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')
#     else:
#         form = ReservationForm()
    
#     return render(request, 'reservation_form.html', {'form': form})