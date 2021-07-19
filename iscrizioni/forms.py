from django import forms
from django.http import request
from .models import Iscrizione
from bambini.models import Bambino
from .models import Iscrizione


class IscrizioneCreateForm(forms.ModelForm):
    class Meta:
        model = Iscrizione
        fields = ['nome', 'bambino']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs) 
        self.fields['bambino'].queryset = self.fields['bambino'].queryset.filter(user=user)
