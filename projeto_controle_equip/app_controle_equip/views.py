from django.shortcuts import render,redirect
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

def gerenciarreservas(request):
     #exibir as reservas em nova pagina
    reservas = {
        'reservas': Reserva.objects.all()
    }
    #retornar os dados para a pagina listagem de reservas
    return render(request,'reservas/reservas.html', reservas)

def editar(request, id_reserva):
    reserva = Reserva.objects.get(id_reserva=id_reserva)
    return render(request,'reservas/update.html', {"reserva": reserva})

def update(request, id_reserva):
    nova_reserva = Reserva()
    vnome=nova_reserva.nome = request.POST.get('nome')
    vmaterial=nova_reserva.material = request.POST.get('material')
    vdata=nova_reserva.data = request.POST.get('data')
    vsala=nova_reserva.sala = request.POST.get('sala')
    nova_reserva = Reserva.objects.get(id_reserva=id_reserva)
    nova_reserva.nome = vnome
    nova_reserva.material = vmaterial
    nova_reserva.data = vdata
    nova_reserva.sala = vsala
    nova_reserva.save()
    return redirect(home)

def delete(request, id_reserva):
    reserva = Reserva.objects.get(id_reserva=id_reserva)
    reserva.delete()
    return redirect(home)
    