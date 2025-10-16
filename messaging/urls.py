# messaging/urls.py
from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),  # Ruta para la bandeja de entrada
    path('compose/', views.compose, name='compose'),  # Ruta para la creación de mensajes
]
