from django.shortcuts import render, redirect
from .models import Bug

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.urls import reverse_lazy

# Create your views here.

class login(LoginView):
    template_name = 'bug_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('appList')

class appList(LoginRequiredMixin, ListView):
    model = Bug
    context_object_name = 'bug'

class appDetail(LoginRequiredMixin, DetailView):
    model = Bug
    context_object_name = 'bug'

class appCreate(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('appList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class appUpdate(LoginRequiredMixin, UpdateView):
    model = Bug
    context_object_name = 'bug'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('appList')

class appDelete(LoginRequiredMixin, DeleteView):
    model = Bug
    context_object_name = 'bug'
    success_url = reverse_lazy('appList')