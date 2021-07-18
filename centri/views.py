from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Centro
from django.urls import reverse_lazy
# Create your views here.


class CentroDetail(DetailView):
    model = Centro
    template_name = 'centro_detail.html'


class CentroList(ListView):
    model = Centro
    template_name = 'centro_list.html'
