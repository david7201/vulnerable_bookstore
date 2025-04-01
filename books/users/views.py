from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import UserProfile

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    
def view_profile(request, profile_id):
    # Retrieve the profile based on its primary key.
    profile = get_object_or_404(UserProfile, pk=profile_id)
    return render(request, 'users/view_profile.html', {'profile': profile})