from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Iscrizione
from django.urls import reverse_lazy
# Create your views here.


class IscrizioneUpdate(UpdateView):
    model = Iscrizione
    template_name = 'iscrizione_update.html'
    fields = ['nome']
    success_url = reverse_lazy("iscrizioni_list")


class IscrizioneList(ListView):
    model = Iscrizione
    template_name = 'iscrizione_list.html'

    def get_queryset(self):
        return self.model.objects.filter(bambino__user=self.request.user)


class IscrizioneCreate(CreateView):
    model = Iscrizione
    fields = ['nome','bambino']
    template_name = 'iscrizione_create.html'
    success_url = reverse_lazy("iscrizioni_list")


class IscrizioneDelete(DeleteView):
    model = Iscrizione
    template_name = 'iscrizione_confirm_delete.html'
    success_url = reverse_lazy('iscrizioni_list')
