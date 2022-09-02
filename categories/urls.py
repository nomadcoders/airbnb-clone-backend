from django.urls import path
from . import views


urlpatterns = [
    path("", views.categories),
    path("<int:pk>", views.category),
]
