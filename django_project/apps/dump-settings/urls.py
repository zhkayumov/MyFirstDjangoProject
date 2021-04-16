from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_settings, name='show_settings')
]
