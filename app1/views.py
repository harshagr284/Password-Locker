from django.shortcuts import render
from app1.models import Password1
from app1.forms import Passform
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
class Indexview(TemplateView):
    template_name='index.html'
class Passlist(LoginRequiredMixin,ListView):
    model=Password1
    context_object_name='pass_list'
    template_name='pass_list.html'
class Passdetail(LoginRequiredMixin,DetailView):
    model=Password1
    context_object_name='pass_detail'
    template_name='pass_detail.html'
class Passcreate(LoginRequiredMixin,CreateView):
    model=Password1
    form_class=Passform
    template_name='pass_form.html'
class Passupdate(LoginRequiredMixin,UpdateView):
    model=Password1
    form_class=Passform
    template_name='pass_form.html'
class Passdelete(LoginRequiredMixin,DeleteView):
    model=Password1
    template_name='pass_delete.html'
    success_url=reverse_lazy('list')
