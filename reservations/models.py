from django.db import models
from django.contrib.auth.models import User

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField()

    def __str__(self):
        return f'Mesa {self.numero}'

class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    pessoas = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reserva para {self.nome} na mesa {self.mesa.numero} para {self.pessoas} pessoas'

class HistoricoReserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Histórico de {self.cliente.username} - Reserva {self.reserva.id}'
