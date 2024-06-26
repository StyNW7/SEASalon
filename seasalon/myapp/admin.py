# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomRole
from .forms import CustomRoleCreationForm, CustomRoleChangeForm

# Custom Role for Admin

class CustomRoleAdmin(UserAdmin):
    add_form = CustomRoleCreationForm
    form = CustomRoleChangeForm
    model = CustomRole
    list_display = ['username', 'email', 'phone_number', 'role']

admin.site.register(CustomRole, CustomRoleAdmin)
