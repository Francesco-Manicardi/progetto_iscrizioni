from django.forms.models import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Iscrizione
from django.urls import reverse_lazy
from centri.models import Centro
from django.contrib import messages
from bambini.models import Bambino
from .forms import IscrizioneCreateForm


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
    form_class = IscrizioneCreateForm
    template_name = 'iscrizione_create.html'
    success_url = reverse_lazy("iscrizioni_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # hack per perfezionisti con una deadline
    def form_valid(self, form):
        form.instance.centro = get_object_or_404(
            Centro, id=self.kwargs['centro_id']
        )
        return super().form_valid(form)


class IscrizioneDelete(DeleteView):
    model = Iscrizione
    template_name = 'iscrizione_confirm_delete.html'
    success_url = reverse_lazy('iscrizioni_list')


def redirectToCentriListWithMessage(request):
    messages.info(
        request, 'Scegli un centro estivo per effettuare una iscrizione.')
    return redirect(to=reverse_lazy("centri_list"))
