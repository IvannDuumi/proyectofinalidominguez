from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def inbox(request):
    msgs = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'messaging/inbox.html', {'messages': msgs})
