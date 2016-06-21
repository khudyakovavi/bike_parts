# coding: utf-8
from django.conf.urls import url

from .views import BikePartAdView, MainView

urlpatterns = [
    url(r'^$', MainView.as_view()),
    url(r'^parts/$', BikePartAdView.as_view()),
]
