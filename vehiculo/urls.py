from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'vehiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.add_vehiculo, name='add_vehiculo'),
    path('vehiculo/list/', views.list_vehiculos, name='list_vehiculos'),
    path('login/', auth_views.LoginView.as_view(template_name='vehiculo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
