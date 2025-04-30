from django.urls import path
from .views import jardim_view

urlpatterns = [
    path('', jardim_view, name="jardim"),
]