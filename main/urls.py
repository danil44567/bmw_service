from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("promo", views.promo, name="promo"),
    path("promo/<int:promo_id>", views.promo_info, name="promo_info")
]