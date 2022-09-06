"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('sound/', include('sound.urls'))
"""
import sound.views
from django.contrib import admin
from django.urls import path, include,re_path

urlpatterns = [
    re_path(r'', include('sound.urls'), name='home'),
    re_path(r'^contact/$', sound.views.contact, name='contact'),
    re_path(r'^termes/$', sound.views.contact, name='termes'),
    re_path(r'^file/$', sound.views.home, name='file'),


]
