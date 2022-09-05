from django.urls import path
from .views import PerkDetail, Perks

urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view()),
]
