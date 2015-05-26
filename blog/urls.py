__author__ = 'amy'
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.post_list),
]
