# coding: utf-8
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from common.constants import PAGE_SIZE
from parts.models import BikePart


class BikePartsPagination(PageNumberPagination):

    page_size = PAGE_SIZE


class BikePartsSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=256)
    brand_name = serializers.CharField(max_length=100, write_only=True)
    brand = serializers.CharField(max_length=100, read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=8,
                                     min_value=0, required=False)
    contacts = serializers.CharField(max_length=100, read_only=True)
    email = serializers.EmailField(max_length=86, required=False,
                                   write_only=True)
    phone = serializers.CharField(max_length=12, required=False,
                                  write_only=True)

    class Meta:
        model = BikePart
        fields = ['name', 'brand', 'price', 'contacts']

    def validate(self, data):
        if not any([data.get('phone'), data.get('email')]):
            raise serializers.ValidationError('Должно быть заполнено хотя бы '
                                              'одно поле с контактами.')
        return super(BikePartsSerializer, self).validate(data)

    def create(self, validated_data):
        return BikePart.objects.create(**validated_data)


class BikePartList(ListAPIView):

    serializer_class = BikePartsSerializer
    pagination_class = BikePartsPagination

    def get_queryset(self):
        queryset = BikePart.objects.all()
        name = self.request.query_params.get('name')
        brand = self.request.query_params.get('brand')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if brand is not None:
            queryset = queryset.filter(brand__name__icontains=brand)
        return queryset


class BikePartAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = BikePartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
