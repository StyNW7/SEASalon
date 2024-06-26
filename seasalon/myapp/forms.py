# seasalon/forms.py

from django import forms
from .models import Reservation, Review, Branch, Service, CustomRole


# Review Form


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer_name', 'star_rating', 'comment']
        exclude = ['customer_name']

    def clean_star_rating(self):
        star_rating = self.cleaned_data.get('star_rating')
        if star_rating < 1 or star_rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return star_rating


# Reservation Form


class ReservationForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=True)
    service = forms.ModelChoiceField(queryset=Service.objects.none(), required=True)
    reservation_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Reservation
        fields = ['branch', 'service', 'reservation_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'branch' in self.data:
            try:
                branch_id = int(self.data.get('branch'))
                self.fields['service'].queryset = Service.objects.filter(branch_id=branch_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['service'].queryset = self.instance.branch.service_set.order_by('name')


# Custom Role Form


class CustomRoleChangeForm(forms.ModelForm):
    class Meta:
        model = CustomRole
        fields = ('username', 'email', 'phone_number', 'role')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .models import CustomRole

class CustomRoleCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)
    role = forms.CharField(max_length=50, initial='customer', widget=forms.HiddenInput())

    class Meta:
        model = CustomRole
        fields = ('username', 'email', 'full_name', 'phone_number', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.role = 'customer'  # Set role to 'customer' explicitly
        if commit:
            user.save()
        return user

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


# Branch Form


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'location', 'opening_time', 'closing_time']


# Service Form


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'duration', 'branch']
