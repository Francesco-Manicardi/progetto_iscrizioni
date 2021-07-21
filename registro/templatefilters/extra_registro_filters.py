from django import template
from ..models import Assenza
from configurazioni.models import Configurazione
from orari.models import Orario
from tariffe.models import Tariffa
from bambini.models import Bambino
from periodi.models import Periodo
register = template.Library()


@register.simple_tag(takes_context=True)
def is_assente(context):
    orario = context['orario']
    bambino = context['bambino']
    data = context['data_registro']
    assente_query = Assenza.objects.filter(
        data=data, orario=orario, bambino=bambino)
    if assente_query.exists():
        return assente_query.first().id
    return 0


@register.simple_tag(takes_context=True)
def is_enrolled(context):
    bambino = context['bambino']
    orario = context['orario']
    periodo = context['periodo']
    configurazioni = Configurazione.objects.filter(
        iscrizione__bambino=bambino, periodo=periodo)
    tariffe = [config.tariffa for config in configurazioni]
    return Orario.objects.filter(pk=orario.pk, tariffa__in=tariffe).exists()
