from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def inbox(request):
    # Mostrar los mensajes en la bandeja de entrada
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html', {'messages': messages})

def compose(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # El usuario logueado es el remitente
            message.is_read = False  # Establecer el valor predeterminado para el campo is_read
            message.save()
            return redirect('messaging:inbox')  # Redirige a la bandeja de entrada
    else:
        form = MessageForm()
    return render(request, 'messaging/compose.html', {'form': form})
