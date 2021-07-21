import datetime

from django.http.response import HttpResponseRedirect
from django.views.generic.detail import DetailView
from iscrizioni.models import Iscrizione
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.urls import reverse_lazy


class IscrizionePaymentCompleted(DetailView):
    model = Iscrizione
    template_name = 'payment_completed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        iscrizione_pagata = self.get_object()
        if not iscrizione_pagata.payed_at:
            iscrizione_pagata.payed_at = datetime.date.today()
            iscrizione_pagata.save()
        return context


class PaymentsList(ListView):
    model = Iscrizione
    template_name = 'payments_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(payed_at__isnull=False)

    def dispatch(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            if u.is_superuser or request.user.groups.filter(name='afc').exists():
                return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("login"))
