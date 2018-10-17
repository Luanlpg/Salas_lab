from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('salas/', views.SalasListView.as_view(), name='salas'),
    path('salas/<int:pk>/', views.SalasDetailView.as_view()),
    path('agendamentos/', views.AgendamentosListView.as_view(), name='agendamentos'),
    path('agendamentos/<int:pk>/', views.AgendamentosDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
