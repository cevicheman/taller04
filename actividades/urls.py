from django.urls import path
from . import views

urlpatterns = [
   path("", views.DemoRestApi.as_view(), name="actividades"),
]