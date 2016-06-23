# coding: utf-8
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from parts.models import BikePart


class BikePartsPagination(PageNumberPagination):

    page_size = 10


class BikePartsSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    brand = serializers.CharField(read_only=True)
    price = serializers.CharField(read_only=True)
    contacts = serializers.CharField(read_only=True)

    class Meta:
        model = BikePart
        fields = ['name', 'brand', 'price', 'contacts']


class BikePartList(ListAPIView):
    queryset = BikePart.objects.all()
    serializer_class = BikePartsSerializer
    pagination_class = BikePartsPagination
