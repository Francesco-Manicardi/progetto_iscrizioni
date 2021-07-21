from django.urls import path
from .views import RegistroIndex, RegistroView, toggle_assenza
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("index", login_required(RegistroIndex.as_view()), name="registro_index"),
    path("<int:pk>/<int:centro_id>/<int:giorno>",
         login_required(RegistroView.as_view()), name="registro_view"),
    path("toggle/<int:orario>/<int:assenza>/<int:periodo_id>/<int:offset_giorno>/<int:bambino>", toggle_assenza, name="toggle_assenza"),
]
