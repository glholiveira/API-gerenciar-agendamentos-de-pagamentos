from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('agendamentos/<int:id>/', views.agendamento_detail, name='agendamento_detail'),
]
