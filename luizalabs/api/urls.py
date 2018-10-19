from django.urls import path
from django.urls import include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('salas/', views.SalasListView.as_view(), name='salas'),
    path('salas/<int:pk>/', views.SalasDetailView.as_view()),
    path('agendar/', views.AgendarView.as_view()),
    path('agendamentos/', views.AgendamentosListView.as_view(), name='agendamentos'),
    path('agendamentos/<int:pk>/', views.AgendamentosDetailView.as_view()),
    path('logs/', views.LogsListView.as_view(), name='logs'),
]
