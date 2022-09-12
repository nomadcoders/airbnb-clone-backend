from django.urls import path
from .views import Wishlists

urlpatterns = [
    path("", Wishlists.as_view()),
]
