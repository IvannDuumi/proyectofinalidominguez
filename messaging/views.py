from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm


@login_required
def send_message(request, recipient_id):
    recipient = User.objects.get(id=recipient_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('messaging:inbox')  
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form, 'recipient': recipient})
