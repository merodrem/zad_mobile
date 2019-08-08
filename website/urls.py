
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='flash_info'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('articles/<int:id>', views.article),
    # path('qui', views.qui, name='qui'),
    # path('pourquoi', views.pourquoi, name='pourquoi'),
]
