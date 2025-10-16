from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Message
from .forms import MessageForm

def inbox(request):
    # Mostrar los mensajes en la bandeja de entrada
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html', {'messages': messages})

def compose(request):
=======
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm


@login_required
def send_message(request, recipient_id):
    recipient = User.objects.get(id=recipient_id)
>>>>>>> 534342b4ae5503d6dd2e2af41764a4d597df42f3
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
<<<<<<< HEAD
            message.sender = request.user  # El usuario logueado es el remitente
            message.is_read = False  # Establecer el valor predeterminado para el campo is_read
            message.save()
            return redirect('messaging:inbox')  # Redirige a la bandeja de entrada
    else:
        form = MessageForm()
    return render(request, 'messaging/compose.html', {'form': form})
=======
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('messaging:inbox')  
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form, 'recipient': recipient})
>>>>>>> 534342b4ae5503d6dd2e2af41764a4d597df42f3
