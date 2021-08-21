from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mynameView, name='home'),
    path('success', views.successfulMsg, name='success'),
]
