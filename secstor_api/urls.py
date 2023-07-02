from django.urls import path
from . import views

urlpatterns = [
    path('', views.anonymize),
    path('r', views.result),
    path('doc', views.doc)
]
