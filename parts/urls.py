# coding: utf-8
from __future__ import absolute_import

from django.conf.urls import url

from .views import MainView

urlpatterns = [
    url(r'^$', MainView.as_view()),
]
