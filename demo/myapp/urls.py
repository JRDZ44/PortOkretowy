from django.urls import path, include
from .views import authView, start, home, delivery, container_counter, port_status_view, export_view, success_view

app_name = 'myapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('', start, name='start'),
    path('signup/', authView, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/delivery/', delivery, name='home/delivery/'),
    path('home/container_counter/', container_counter, name='container_counter'),
    path('home/ports_status/', port_status_view, name='ports_status'),
    path('home/export_view/', export_view, name='export_view'),
    path('success/', success_view, name='success_view'),
]