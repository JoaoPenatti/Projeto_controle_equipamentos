
from django.urls import path
from app_controle_equip import views

urlpatterns = [
    #rota (vazia por nao ter nada após a barra), view responsavel (view criada que sera carregada na rota), nome de referencia
   path('',views.home,name='home'),

   path('reservas/',views.reservas,name='listagem_reservas'),
]
