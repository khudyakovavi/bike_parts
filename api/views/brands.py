# coding: utf-8
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from rest_framework.generics import ListAPIView

from brands.models import BikeBrand


class BikeBrandSerializer(serializers.Serializer):

    name = serializers.CharField(read_only=True)
    parts_qty = serializers.IntegerField(read_only=True)

    class Meta:
        model = BikeBrand
        fields = ['name', 'parts_qty']


class BikeBrandList(ListAPIView):

    queryset = BikeBrand.objects.get_popular()
    serializer_class = BikeBrandSerializer
