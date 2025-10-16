from django.shortcuts import render, redirect
from .forms import SignUpForm  

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('accounts:login')  
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
<<<<<<< HEAD


@login_required
def profile_view(request):
    """Muestra el perfil del usuario logueado."""
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Edición del perfil (incluye avatar y ahora nombre y apellido)."""
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)
=======
>>>>>>> a59227e5c5c30dd1ae5685e3d4ce921d8ce9bf8d
