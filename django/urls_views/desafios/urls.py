from django.urls import path
from .views import domingo, segunda, terça

urlpatterns = [
    path("domingo", domingo),
    path("segunda", segunda),
    path("terça", terça),
]
