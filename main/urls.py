from django.contrib import admin
from django.urls import path, include

from .views import GeneralPage

urlpatterns = [
    path('', GeneralPage.as_view(), name='home'),
]
