from iscrizioni.models import Iscrizione
from django import forms
from .models import Configurazione
from .models import Configurazione
from django.shortcuts import get_object_or_404


class ConfigurazioneCreateForm(forms.ModelForm):
    class Meta:
        model = Configurazione
        fields = ['periodo', 'tariffa']

    def __init__(self, *args, **kwargs):
        iscrizione_id = kwargs.pop('iscrizione_id', None)
        iscrizione = get_object_or_404(Iscrizione, id=iscrizione_id)
        super().__init__(*args, **kwargs)

        # si possono configurare solo i periodi per i quali non è ancora stata fatta una configurazione
        periodi_gia_configurati = iscrizione.get_periodi()

        self.fields['periodo'].queryset = self.fields['periodo'].queryset.exclude(
            pk__in=[periodo.id for periodo in periodi_gia_configurati]
        )
