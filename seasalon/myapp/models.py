# seasalon/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser


# Custom Role Model (Admin and Customer) based on the question's guide


class CustomRole(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


# Branch Model based on the question's guide


class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


# Service Model based on the question's guide


class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.branch.name})"


# Reservation Model based on the question's guide

from django.core.exceptions import ValidationError
from django.utils import timezone

class Reservation(models.Model):
    user = models.ForeignKey(CustomRole, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.user.full_name} at {self.branch.name} on {self.reservation_time}"

    def clean(self):
        super().clean()
        if self.service and self.reservation_time:
            opening_time = self.branch.opening_time
            closing_time = self.branch.closing_time
            reservation_time = self.reservation_time.time()

            if not (opening_time <= reservation_time <= closing_time):
                raise ValidationError(f"Reservation time must be between {opening_time} and {closing_time}")



# Review Model based on the question's guide


class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    star_rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.customer_name} - {self.star_rating} stars'
