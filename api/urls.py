from django.urls import path
from . import views

urlpatterns = [
    path('', views.anonymize),
    path('help',  views.help),
]
