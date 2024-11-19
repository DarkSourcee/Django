# reservations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('reservar/', views.reservar_mesa, name='reservar_mesa'),
    path('historico/', views.historico_reservas, name='historico_reservas'),
    path('dash/', views.dashboard_admin, name='dash'),
]
