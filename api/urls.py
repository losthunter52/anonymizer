from django.urls import path
from . import views

urlpatterns = [
    path('', views.anonymize),
    path('doc', views.doc)
]
