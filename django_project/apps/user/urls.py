from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_user, name='hello_user')
]
