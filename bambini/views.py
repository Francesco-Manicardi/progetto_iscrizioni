from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Bambino
# Create your views here.

class BambinoDetail(DetailView):
    model = Bambino
    template_name = 'bambino_detail.html'
