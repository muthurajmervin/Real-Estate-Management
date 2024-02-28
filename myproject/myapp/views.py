from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Property, Unit, Tenant
from .forms import LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Unit, Tenant
from .forms import PropertyForm, UnitForm, TenantForm
from .models import Tenant, Unit
from .forms import TenantForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('property_list'))  # Redirect to property list view after successful login
        # If authentication fails, display error message
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

# Implement other views for property, unit, and tenant management functionalities



# Property Detail View
def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'property_detail.html', {'property': property})

# Unit Detail View
def unit_detail(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    return render(request, 'unit_detail.html', {'unit': unit})

# Tenant Management View
def tenant_management(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_management.html', {'tenants': tenants})

# Add Property View
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

# Add Unit View
def add_unit(request, property_id):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = get_object_or_404(Property, pk=property_id)
            unit.save()
            return redirect('property_detail', property_id=property_id)
    else:
        form = UnitForm()
    return render(request, 'add_unit.html', {'form': form})

# Add Tenant View


def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = TenantForm()
    
    # Get available units
    units = Unit.objects.all()
    
    return render(request, 'add_tenant.html', {'form': form, 'units': units})


