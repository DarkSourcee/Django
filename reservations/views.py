# reservations/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ReservaForm
from .models import Mesa, Reserva
from django.contrib import messages

# Cadastro de Cliente
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login de Cliente
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dash') 
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Realizar a reserva de mesa
def reservar_mesa(request):
    mesas = Mesa.objects.all() 
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cliente = request.user 
            reserva.save() 
            return redirect('historico_reservas') 
    else:
        form = ReservaForm()

    return render(request, 'reservation_form.html', {'form': form, 'mesas': mesas})

def dashboard_client(request):
    if not request.user.is_authenticated:
        return redirect('login')

    reservas = Reserva.objects.filter(cliente=request.user)
    return render(request, 'dashboard_client.html', {'reservas': reservas})

def historico_reservas(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    
    reservas = Reserva.objects.filter(cliente=request.user)

    return render(request, 'history_reservations.html', {'reservas': reservas})

# Dashboard Administrativo (Gestão de Reservas)
from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def dashboard_admin(request):
    reservas = Reserva.objects.all()
    return render(request, 'dashboard_admin.html', {'reservas': reservas})
