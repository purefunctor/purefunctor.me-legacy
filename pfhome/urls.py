from django.urls import path
from pfhome import views

urlpatterns = [
    path("", views.soon),
]
