# messaging/urls.py
from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
<<<<<<< HEAD
    path('inbox/', views.inbox, name='inbox'),  # Ruta para la bandeja de entrada
    path('compose/', views.compose, name='compose'),  # Ruta para la creación de mensajes
=======
    path('send/<int:recipient_id>/', views.send_message, name='send_message'),
>>>>>>> 534342b4ae5503d6dd2e2af41764a4d597df42f3
]
