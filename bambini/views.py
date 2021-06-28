from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Bambino
from django.urls import reverse_lazy
# Create your views here.


class BambinoDetail(DetailView):
    model = Bambino
    template_name = 'bambino_detail.html'


class BambinoList(ListView):
    model = Bambino
    template_name = 'bambino_list.html'


class BambinoCreate(CreateView):
    model = Bambino
    fields = ('nome', 'cognome')
    template_name = 'bambino_create.html'
    success_url = reverse_lazy("bambini_list")
