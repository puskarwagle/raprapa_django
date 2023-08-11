from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_membership", views.submit_membership, name="submit_membership"),
    path("payment/", views.payment_page, name="payment"),
    path("initiate_khalti_payment", views.initiate_khalti_payment, name="initiate_khalti_payment"),
    path("id_card/", views.id_card, name="id_card"),
]