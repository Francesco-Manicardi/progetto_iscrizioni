from django.urls import path
from .views import BambinoDetail
urlpatterns = [
    path("<int:pk>", BambinoDetail.as_view(), name="bambini_detail")
]
