from django.urls import path
from .views import IscrizioneDelete, IscrizioneUpdate, IscrizioneList, IscrizioneCreate, redirectToCentriListWithMessage
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("<int:pk>", login_required(IscrizioneUpdate.as_view()), name="iscrizioni_update"),
    path("delete/<int:pk>", login_required(IscrizioneDelete.as_view()), name="iscrizioni_delete"),
    path("", login_required(IscrizioneList.as_view()), name="iscrizioni_list"),
    path("create/<int:centro_id>", login_required(IscrizioneCreate.as_view()), name="iscrizioni_create"),
    path("create", login_required(redirectToCentriListWithMessage), name="iscrizioni_create_without_centro")
]
