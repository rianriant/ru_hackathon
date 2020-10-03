from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.models import User
from .models import Ivent
from .forms import IventCreateForm
from users.models import Profile


class IventListView(ListView):
    """ListView for listing ivents onto the homepage"""
    #model = Ivent
    template_name = 'main/homepage.html'
    context_object_name = 'ivents'
    ordering = ['-date_posted']
    paginate = 10

    def get_queryset(self, *args, **kwargs):
        area_var = self.request.GET.get('area', None)
        if area_var is not None:
            qset = Ivent.objects.filter(area=area_var)
        else:
            qset = Ivent.objects.all()
        return qset

class IventCreateView(LoginRequiredMixin, CreateView):
    """CreateView for creating an event announcement"""
    model = Ivent
    form_class = IventCreateForm
    template_name = 'main/create_ivent.html'
    login_url = '/login/'
    redirect_field_name = 'login'

    # The method that handles processes related to saving model instance
    def form_valid(self, form):
        form.instance.created_by = Profile.objects.get(user=self.request.user)
        if form.is_valid():
            messages.success(self.request, 'Событие созданно!')
        return super().form_valid(form)

class IventDetailView(DetailView):
    """This DetailView maintains pages of distinct ivents"""
    model = Ivent
    template_name = 'main/ivent_detail.html'
