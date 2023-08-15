from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_membership", views.submit_membership, name="submit_membership"),
    path("payment/", views.payment_page, name="payment"),
    path('initiate_khalti_payment/', views.initiate_khalti_payment, name='initiate_khalti_payment'),
    path("id_card/", views.id_card, name="id_card"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
