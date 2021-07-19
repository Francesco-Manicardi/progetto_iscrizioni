from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Configurazione
from django.urls import reverse_lazy
from iscrizioni.models import Iscrizione
from django.contrib import messages
from .forms import ConfigurazioneCreateForm


class ConfigurazioneUpdate(UpdateView):
    model = Configurazione
    template_name = 'configurazione_update.html'
    fields = ['nome']
    success_url = reverse_lazy("configurazioni_list")

class ConfigurazioneCreate(CreateView):
    model = Configurazione
    form_class = ConfigurazioneCreateForm
    template_name = 'configurazione_create.html'
    
    def get_success_url(self, **kwargs): 
        return reverse_lazy("iscrizioni_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'iscrizione_id': self.kwargs['iscrizione_id']})
        return kwargs

    # hack per perfezionisti con una deadline
    def form_valid(self, form):
        form.instance.iscrizione = get_object_or_404(
            Iscrizione, id=self.kwargs['iscrizione_id']
        )
        return super().form_valid(form)


class ConfigurazioneDelete(DeleteView):
    model = Configurazione
    template_name = 'configurazione_confirm_delete.html'
    success_url = reverse_lazy('configurazioni_list')


def redirectToCentriListWithMessage(request):
    messages.info(
        request, 'Scegli un iscrizione estivo per effettuare una configurazione.')
    return redirect(to=reverse_lazy("centri_list"))
