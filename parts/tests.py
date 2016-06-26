# coding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from parts.forms import BikePartForm
from parts.models import BikePart


class BikePartListTestCase(TestCase):

    def setUp(self):
        data = [
            {'name': 'Руль', 'brand_name': 'Vinca',
             'price': 100, 'email': 'test@test.ru'},
            {'name': 'Педали', 'brand_name': 'BBB',
             'price': 50, 'phone': '+7123123123'},
            {'name': 'Седло', 'brand_name': 'Mizumi',
             'price': 100, 'email': 'test@test.ru'},
            {'name': 'Руль', 'brand_name': 'Mizumi',
             'price': 100, 'email': 'test1@test.ru'},
            {'name': 'Disk Brakes', 'brand_name': 'Shimano',
             'price': 100, 'email': 'test1@test.ru'}
        ]
        for item in data:
            part = BikePart.objects.create(**item)
            part.save()

    def assert_parts_quantity(self, url, quantity):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        bike_parts = response.context_data.get('bike_parts').object_list
        self.assertEqual(len(bike_parts), quantity)

    def test_get_list(self):
        self.assert_parts_quantity(reverse('parts:parts_list'), 5)

    def test_search_by_name(self):
        url = '{}?search={}'.format(reverse('parts:parts_list'), 'Руль')
        self.assert_parts_quantity(url, 2)

    def test_search_by_name_not_found(self):
        url = '{}?search={}'.format(reverse('parts:parts_list'), '123')
        self.assert_parts_quantity(url, 0)

    def test_search_by_name_case_insensitive(self):
        url = '{}?search={}'.format(reverse('parts:parts_list'), 'disk')
        self.assert_parts_quantity(url, 1)

    def test_search_by_name_case_insensitive_rus(self):
        # т.к. используется SQLite, не поддерживается регистронезависимый
        # поиск по символам, выходящим за пределам ASCII
        url = '{}?search={}'.format(reverse('parts:parts_list'), 'седло')
        self.assert_parts_quantity(url, 0)

    def test_search_by_brand(self):
        url = '{}?search={}'.format(reverse('parts:parts_list'), 'Vinca')
        self.assert_parts_quantity(url, 1)

    def test_search_by_brand_not_found(self):
        url = '{}?search={}'.format(reverse('parts:parts_list'), '123')
        self.assert_parts_quantity(url, 0)


class BikePartFormTestCase(TestCase):
    # Тесты валидации формы создания объяления

    def test_part_valid(self):
        data = [
            {'name': 'Руль', 'brand_name': 'Vinca',
             'price': 100, 'email': 'test@test.ru'},
            {'name': 'Руль', 'brand_name': 'Vinca',
             'email': 'test@test.ru'},
            {'name': 'Педали', 'brand_name': 'BBB',
             'price': 50, 'phone': '+7123123123'},
            {'name': 'Седло', 'brand_name': 'Mizumi',
             'price': 100, 'email': 'test@test.ru'},
            {'name': 'Руль', 'brand_name': 'Mizumi',
             'price': 100, 'email': 'test1@test.ru'},
            {'name': 'Disk Brakes', 'brand_name': 'Shimano',
             'price': 100, 'email': 'test1@test.ru', 'phone': '71231231238'}
        ]
        for item in data:
            form = BikePartForm(item)
            self.assertTrue(form.is_valid())

    def test_empty_params(self):
        form = BikePartForm({})
        self.assertFalse(form.is_valid())

    def test_no_brand_name(self):
        form = BikePartForm({'name': 'Педали', 'price': 50,
                             'phone': '+7123123123'})
        self.assertFalse(form.is_valid())

    def test_no_part_name(self):
        form = BikePartForm({'brand_name': 'Mizumi', 'price': 50,
                             'phone': '+7123123123'})
        self.assertFalse(form.is_valid())

    def test_no_contacts(self):
        form = BikePartForm({'name': 'Седло', 'brand_name': 'Mizumi',
                             'price': 50})
        self.assertFalse(form.is_valid())

    def test_incorrect_email(self):
        form = BikePartForm({'name': 'Седло', 'brand_name': 'Mizumi',
                             'price': 100, 'email': 'test'})
        self.assertFalse(form.is_valid())

    def test_negative_price(self):
        form = BikePartForm({'name': 'Седло', 'brand_name': 'Mizumi',
                             'price': -1, 'email': 'test'})
        self.assertFalse(form.is_valid())
