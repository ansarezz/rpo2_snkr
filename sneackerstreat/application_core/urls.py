from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_page, name = "model_page")
]