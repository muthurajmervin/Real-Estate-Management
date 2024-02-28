from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    Features=models.CharField(max_length=100, default='No features specified')

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=10, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')])

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='tenants')
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()


class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
