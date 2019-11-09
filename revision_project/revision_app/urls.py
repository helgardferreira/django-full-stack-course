from django.urls import path

from revision_app import views

urlpatterns = [path("", views.index)]
