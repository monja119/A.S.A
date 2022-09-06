from . import views
from django.urls import path, re_path

app_name = 'sound'
urlpatterns = [
    re_path(r'^$', views.home,name='home'),
    re_path(r'^acceuil/$', views.home)
]
