from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('send/<int:recipient_id>/', views.send_message, name='send_message'),
]
