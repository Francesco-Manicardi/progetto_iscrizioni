from django.http.response import HttpResponse
from registro.models import Assenza
from django.contrib.auth.decorators import login_required
from iscrizioni.models import Iscrizione
from configurazioni.models import Configurazione
from periodi.models import Periodo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from centri.models import Centro
from orari.models import Orario
from bambini.models import Bambino


class RegistroIndex(ListView):
    model = Centro
    template_name = 'registro_index.html'


class RegistroView(DetailView):
    model = Periodo
    template_name = 'registro_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        periodo = self.get_object()
        offset_giorno = self.kwargs["giorno"]
        context["offset_giorno"] = offset_giorno
        context["data_registro"] = periodo.get_nesima_data(offset_giorno)
        context["orari"] = Orario.objects.all()

        centro = Centro.objects.get(pk=self.kwargs["centro_id"])

        configurazioni_del_periodo = Configurazione.objects.filter(
            periodo=periodo)

        iscrizioni_da_mostrare = Iscrizione.objects.filter(
            configurazione__in=configurazioni_del_periodo, centro=centro).all()

        context["bambini"] = Bambino.objects.filter(
            iscrizione__id__in=[iscrizione.id for iscrizione in iscrizioni_da_mostrare]).distinct()
        return context


@login_required
def toggle_assenza(request, orario, assenza, periodo_id, offset_giorno, bambino):
    orario = Orario.objects.filter(pk=orario).first()
    periodo = Periodo.objects.filter(pk=periodo_id).first()
    bambino = Bambino.objects.filter(pk=bambino).first()
    existing_assenza_id = int(assenza)
    data_evento = periodo.get_nesima_data(offset_giorno)

    if(existing_assenza_id > 0):
        assenza_esistente = Assenza.objects.filter(
            pk=existing_assenza_id).delete()
    else:
        assenza = Assenza.objects.create(
            orario=orario, bambino=bambino, data=data_evento)
        assenza.save()
    return HttpResponse("Ok")
