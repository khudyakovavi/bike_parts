# coding: utf-8
from __future__ import absolute_import

from django.conf.urls import url

from .views.brands import BikeBrandList
from .views.parts import BikePartList, BikePartAPIView

urlpatterns = [
    url(r'^part/$', BikePartAPIView.as_view()),
    url(r'^parts/$', BikePartList.as_view()),
    url(r'^brands/$', BikeBrandList.as_view())
]
