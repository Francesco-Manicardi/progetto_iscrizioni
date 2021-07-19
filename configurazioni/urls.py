from django.urls import path
from .views import ConfigurazioneDelete, ConfigurazioneUpdate,  ConfigurazioneCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("<int:pk>", login_required(ConfigurazioneUpdate.as_view()), name="configurazioni_update"),
    path("delete/<int:pk>", login_required(ConfigurazioneDelete.as_view()), name="configurazioni_delete"),
    path("create/<int:iscrizione_id>", login_required(ConfigurazioneCreate.as_view()), name="configurazioni_create"),
]
