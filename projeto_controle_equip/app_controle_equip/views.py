from django.shortcuts import render
from .models import Reserva

def home(request):
    return render(request,'reservas/home.html')

def reservas(request):
    #salvar os dados da tela para o banco
    nova_reserva = Reserva()
    nova_reserva.nome = request.POST.get('nome')
    nova_reserva.material = request.POST.get('material')
    nova_reserva.data = request.POST.get('data')
    nova_reserva.sala = request.POST.get('sala')
    nova_reserva.save()

    #exibir as reservas em nova pagina
    reservas = {
        'reservas': Reserva.objects.all()

    }
    #retornar os dados para a pagina listagem de reservas
    return render(request,'reservas/reservas.html', reservas)
