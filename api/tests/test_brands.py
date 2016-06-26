# coding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from parts.models import BikePart


class BikePartListTestCase(TestCase):

    def setUp(self):
        for i in range(6):
            part = BikePart.objects.create(
                name=str(i),
                price=0,
                brand_name='Mizumi',
                phone='0'
            )
            part.save()
        for i in range(10):
            part = BikePart.objects.create(
                name=str(i),
                price=0,
                brand_name='Vinca',
                phone='0'
            )
            part.save()
        for i in range(5):
            part = BikePart.objects.create(
                name=str(i),
                price=0,
                brand_name='Shimano',
                phone='0'
            )
            part.save()

    def test_get_list_of_popular_brands(self):
        response = self.client.get(reverse('api:popular_brands'))
        self.assertEqual(response.status_code, 200)
        # Популярной считается марка, для которой найдено
        # строго более 5 деталей, следовательно, в результате
        # должно быть 2 записи
        self.assertEqual(len(response.data), 2)
        # Результат должен быть отсортирован по убыванию
        # количества деталей марки
        self.assertEqual(response.data[0]['name'], 'Vinca')
