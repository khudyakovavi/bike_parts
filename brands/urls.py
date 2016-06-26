# coding: utf-8
from __future__ import absolute_import

from django.conf.urls import url

from .views import PopularBrandsView

urlpatterns = [
    url(r'^$', PopularBrandsView.as_view(), name='popular_brands'),
]
