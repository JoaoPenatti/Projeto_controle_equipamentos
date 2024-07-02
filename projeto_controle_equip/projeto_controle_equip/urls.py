from django.urls import path
from app_controle_equip import views

urlpatterns = [
    #rota (vazia por nao ter nada após a barra), view responsavel (view criada que sera carregada na rota), nome de referencia
   path('',views.home,name='home'),

   path('reservas/',views.reservas,name='listagem_reservas'),

   path('gerenciarreservas/',views.gerenciarreservas,name='gerenciar_reservas'),

   path('editar/<int:id_reserva>',views.editar,name='editar'),

   path('update/<int:id_reserva>',views.update,name='update'),
   
   path('delete/<int:id_reserva>',views.delete,name='delete'),
]
