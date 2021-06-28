from django.urls import path
from .views import BambinoDetail, BambinoList, BambinoCreate

urlpatterns = [
    path("<int:pk>", BambinoDetail.as_view(), name="bambini_detail"),
    path("", BambinoList.as_view(), name="bambini_list"),
    path("create", BambinoCreate.as_view(), name="bambini_create")
]
