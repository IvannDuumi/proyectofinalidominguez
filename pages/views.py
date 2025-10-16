from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Page
from .forms import PageForm

@login_required
def page_create_view(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:list')
    else:
        form = PageForm()
    return render(request, 'pages/page_form.html', {'form': form})
