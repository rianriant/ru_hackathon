from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpadateForm,
)
from django.views.generic import (
    DetailView,
    UpdateView,
)

from django.contrib.auth.models import User
from .models import Profile
from main.models import Ivent


# Авторизационный код:
def register(request):
    if request.user.is_authenticated:
        return redirect('ivent-list')
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def update (request):
    print(1)
    current_profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileUpadateForm(request.POST, 
                                    request.FILES, 
                                    instance=current_profile
                                    )
        if form.is_valid():
            form.save()
            messages.success(request, f'Профиль обновлен!')
            return redirect(current_profile.get_absolute_url())  
    else:
        form = ProfileUpadateForm(instance=current_profile)
        
    context = {'form' : form}

    return render(request, 'users/profile_update.html', context)


class ProfileDetailView(DetailView):
    """This detail view maintains user's profile and events he started"""
    model = Profile
    # 'slug' is used for non-id resource identethication.
    # The field slug refers to must be unique
    slug_field = 'user'
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    def get_context_data(self, *args, **kwargs):
        """This function handles additional data to template. Key of the 'context' dictionary is
        name of the relation in the template, in this piece it's 'user_ivents'"""

        context = super().get_context_data()
        context['user_ivents'] = Ivent.objects.filter(created_by=Profile.objects.get(user=self.request.user)).order_by('-date_posted')
        return context

