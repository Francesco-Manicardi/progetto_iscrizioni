from django.urls import path
from .views import IscrizionePaymentCompleted,PaymentsList
from django.contrib.auth.decorators import login_required


urlpatterns = [ 
    path("paypal/completed/<int:pk>", login_required(IscrizionePaymentCompleted.as_view()), name="payments_paypal_completed"), 
    path("sommario", login_required(PaymentsList.as_view()), name="payments_list"), 
]
