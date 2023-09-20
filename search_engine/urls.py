from django.urls import path
from .views import *

urlpatterns = [
    path('s/', fetch_pageedata),
]
