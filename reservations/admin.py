# reservations/admin.py
from django.contrib import admin
from .models import Mesa, Reserva, HistoricoReserva

admin.site.register(Mesa)
admin.site.register(Reserva)
admin.site.register(HistoricoReserva)
