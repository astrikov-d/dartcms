# coding: utf-8
from django.conf.urls import url

from .views import DashboardIndexView

urlpatterns = [
    url(r'^$', DashboardIndexView.as_view(), name='index'),
]
