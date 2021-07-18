from django.urls import path
from .views import CentroDetail, CentroList
urlpatterns = [
    path("<int:pk>", CentroDetail.as_view(), name="centri_detail"),
    path("", CentroList.as_view(), name="centri_list"),
]
