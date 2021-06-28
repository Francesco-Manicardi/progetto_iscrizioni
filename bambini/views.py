from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Bambino
# Create your views here.


class BambinoDetail(DetailView):
    model = Bambino
    template_name = 'bambino_detail.html'


class BambinoList(ListView):
    model = Bambino
    template_name = 'bambino_list.html'
