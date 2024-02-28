from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('property/', views.property_list, name='property_list'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('unit/<int:unit_id>/', views.unit_detail, name='unit_detail'),
    path('tenant/', views.tenant_management, name='tenant_management'),
    path('property/add/', views.add_property, name='add_property'),
    path('property/<int:property_id>/add_unit/', views.add_unit, name='add_unit'),
    path('tenant/add/', views.add_tenant, name='add_tenant'),
    path('signup/', views.signup, name='signup'),
]
