from django.urls import path
from pfhome import views

urlpatterns = [
    path("", views.home),
    path("about/", views.soon),
    path("blog/", views.soon),
]
