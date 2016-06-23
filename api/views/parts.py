# coding: utf-8
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from parts.models import BikePart, BikeBrand


class BikePartsPagination(PageNumberPagination):

    page_size = 10


class BikePartsSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=256)
    brand = serializers.CharField(max_length=100)
    price = serializers.DecimalField(decimal_places=2, max_digits=8)
    contacts = serializers.CharField(max_length=100)

    class Meta:
        model = BikePart
        fields = ['name', 'brand', 'price', 'contacts']

    def create(self, validated_data):
        brand_name = validated_data.get('brand')
        brand = BikeBrand.objects.filter(name=brand_name).first()
        if brand is None:
            brand = BikeBrand(name=brand_name)
            brand.save()
        validated_data['brand'] = brand
        return BikePart.objects.create(**validated_data)


class BikePartList(ListAPIView):

    queryset = BikePart.objects.all()
    serializer_class = BikePartsSerializer
    pagination_class = BikePartsPagination


class BikePartAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = BikePartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
