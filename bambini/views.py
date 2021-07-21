from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Bambino
from django.urls import reverse_lazy
# Create your views here.


class BambinoUpdate(UpdateView):
    model = Bambino
    template_name = 'bambino_update.html'
    fields = ('nome', 'cognome', 'codice_fiscale', 'immagine')
    success_url = reverse_lazy("bambini_list")


class BambinoList(ListView):
    model = Bambino
    template_name = 'bambino_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class BambinoCreate(CreateView):
    model = Bambino
    fields = ('nome', 'cognome', 'codice_fiscale', 'immagine')
    template_name = 'bambino_create.html'
    success_url = reverse_lazy("bambini_list")

    # hack per perfezionisti con una deadline
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BambinoDelete(DeleteView):
    model = Bambino
    template_name = 'bambino_confirm_delete.html'
    success_url = reverse_lazy('bambini_list')
