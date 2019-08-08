
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('flash', views.flash, name='flash'),
    path('article', views.article, name='article'),
    path('position', views.position, name='position'),
    path('reset_location', views.reset_location, name='reset_location'),
]
