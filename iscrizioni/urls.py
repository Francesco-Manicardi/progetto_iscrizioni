from django.urls import path
from .views import IscrizioneDelete, IscrizioneUpdate, IscrizioneList, IscrizioneCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("<int:pk>", login_required(IscrizioneUpdate.as_view()), name="iscrizioni_update"),
    path("delete/<int:pk>", login_required(IscrizioneDelete.as_view()), name="iscrizioni_delete"),
    path("", login_required(IscrizioneList.as_view()), name="iscrizioni_list"),
    path("create", login_required(IscrizioneCreate.as_view()), name="iscrizioni_create")
]
