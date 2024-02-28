from django import forms
from .models import Property, Unit, Tenant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class UnitForm(forms.ModelForm):
    # Define choices list for unit_type field
    UNIT_TYPE_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    ]
    
    # Use ModelChoiceField for unit_type field
    unit_type = forms.ChoiceField(choices=UNIT_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Unit
        fields = ['property', 'rent_cost', 'unit_type']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')    
