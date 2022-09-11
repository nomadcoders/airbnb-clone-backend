from django.urls import path
from .views import PhotoDetail

urlpatterns = [
    path("photos/<int:pk>", PhotoDetail.as_view()),
]
