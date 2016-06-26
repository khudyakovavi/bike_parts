# coding: utf-8
from __future__ import absolute_import

from django.conf.urls import url

from .views import BikePartListView, BikePartView

urlpatterns = [
    url(r'^$', BikePartListView.as_view(), name='parts_list'),
    url(r'^part/new/$', BikePartView.as_view(), name='new_part'),
]
