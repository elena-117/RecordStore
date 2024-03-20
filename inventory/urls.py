from django.urls import path

from inventory.views import home

urlpatterns = [
    path('home/', home)
]
