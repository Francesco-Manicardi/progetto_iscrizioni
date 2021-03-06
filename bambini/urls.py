from django.urls import path
from .views import BambinoDelete, BambinoUpdate, BambinoList, BambinoCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("<int:pk>", login_required(BambinoUpdate.as_view()), name="bambini_update"),
    path("delete/<int:pk>", login_required(BambinoDelete.as_view()), name="bambini_delete"),
    path("", login_required(BambinoList.as_view()), name="bambini_list"),
    path("create", login_required(BambinoCreate.as_view()), name="bambini_create")
]
