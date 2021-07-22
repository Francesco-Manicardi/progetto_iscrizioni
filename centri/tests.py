from django.urls.base import reverse
from bambini.models import Bambino
from iscrizioni.models import Iscrizione
from django.test import TestCase

from django.test import TestCase
from .models import Centro
from django.contrib.auth.models import User
from django.test import Client


class CentroMethodTests(TestCase):
    centro1: Centro
    centro2: Centro
    bambino: Bambino

    def setUp(self):
        super().setUp()
        self.centro1 = Centro(capienza=10, nome="Centro prova 1",
                              indirizzo="Indirizzo test")
        self.centro2 = Centro(capienza=42, nome="Centro prova 2",
                              indirizzo="Indirizzo test")

        self.centro1.save()
        self.centro2.save()

        user = User.objects.create(username="Utente")
        user.save()

        self.bambino = Bambino.objects.create(
            nome="bambino", cognome="test", user=user)
        self.bambino.save()

    def test_riduzione_capacita_residua_centri_estivi(self):
        """
        La capacità residua del centro estivo deve scendere di 1 quando si aggiunge una nuova iscrizione
        """
        old_capacity = self.centro1.get_capienza_residua()

        iscrizione = Iscrizione(nome="Iscrizione test",
                                centro=self.centro1, bambino=self.bambino)
        iscrizione.save()

        new_capacity = self.centro1.get_capienza_residua()

        self.assertEqual(new_capacity, old_capacity-1)

        iscrizione.delete()
        new_capacity = self.centro1.get_capienza_residua()
        self.assertEqual(new_capacity, old_capacity)


    def test_capienza_indipendente_centri_estivi_diversi(self):
        """
        La capacità residua di un centro estivo deve rimanere inalterata se si aggiunge una nuova iscrizione
        a un altro centro estivo
        """

        old_capacity = self.centro1.get_capienza_residua()
        iscrizione = Iscrizione(nome="Iscrizione test",
                                centro=self.centro2, bambino=self.bambino)
        iscrizione.save()

        new_capacity = self.centro1.get_capienza_residua()
        self.assertEqual(old_capacity, new_capacity)

    def test_iscrizione_presente_solo_se_capienza_residua(self):
        c = Client()

        while(self.centro1.get_capienza_residua() > 0):
            response = c.get(reverse('centri_detail', kwargs={"pk": 1}))
            self.assertContains(response, "Iscrivi un bambino a questo centro")
            iscrizione = Iscrizione(nome="Iscrizione test",
                                    centro=self.centro1, bambino=self.bambino)
            iscrizione.save()

        response = c.get(reverse('centri_detail', kwargs={"pk": 1}))
        self.assertNotContains(response, "Iscrivi un bambino a questo centro")
        self.assertContains(
            response, "Le iscrizioni per questo centro estivo sono chiuse: la capienza massima è stata raggiunta.")
