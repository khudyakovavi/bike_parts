# coding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

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
        self.assertEqual(response.data.get('count'), quantity)

    def test_get_list(self):
        self.assert_parts_quantity(reverse('api:parts_list'), 5)

    def test_search_by_name(self):
        url = '{}?name={}'.format(reverse('api:parts_list'), 'Руль')
        self.assert_parts_quantity(url, 2)

    def test_search_by_name_not_found(self):
        url = '{}?name={}'.format(reverse('api:parts_list'), '123')
        self.assert_parts_quantity(url, 0)

    def test_search_by_name_case_insensitive(self):
        url = '{}?name={}'.format(reverse('api:parts_list'), 'disk')
        self.assert_parts_quantity(url, 1)

    def test_search_by_name_case_insensitive_rus(self):
        # т.к. используется SQLite, не поддерживается регистронезависимый
        # поиск по символам, выходящим за пределам ASCII
        url = '{}?name={}'.format(reverse('api:parts_list'), 'седло')
        self.assert_parts_quantity(url, 0)

    def test_search_by_brand(self):
        url = '{}?brand={}'.format(reverse('api:parts_list'), 'Vinca')
        self.assert_parts_quantity(url, 1)

    def test_search_by_brand_not_found(self):
        url = '{}?brand={}'.format(reverse('api:parts_list'), '123')
        self.assert_parts_quantity(url, 0)

    def test_search_by_both(self):
        url = '{}?brand={}&name={}'.format(reverse('api:parts_list'),
                                           'Mizumi', 'Седло')
        self.assert_parts_quantity(url, 1)

    def test_search_by_both_not_found(self):
        url = '{}?brand={}&name={}'.format(reverse('api:parts_list'),
                                           'Vinca', 'Седло')
        self.assert_parts_quantity(url, 0)


class BikePartAPITestCase(TestCase):

    def create_part(self, params, status_code):
        url = reverse('api:new_part')
        response = self.client.post(url, params)
        self.assertEqual(response.status_code, status_code)

    def test_create_part(self):
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
            self.create_part(item, 201)

    def test_empty_params(self):
        self.create_part({}, 400)

    def test_no_brand_name(self):
        description = {'name': 'Педали', 'price': 50, 'phone': '+7123123123'}
        self.create_part(description, 400)

    def test_no_part_name(self):
        description = {'brand_name': 'Mizumi', 'price': 50,
                       'phone': '+7123123123'}
        self.create_part(description, 400)

    def test_no_contacts(self):
        description = {'name': 'Седло', 'brand_name': 'Mizumi', 'price': 50}
        self.create_part(description, 400)

    def test_incorrect_email(self):
        description = {'name': 'Седло', 'brand_name': 'Mizumi',
                       'price': 100, 'email': 'test'}
        self.create_part(description, 400)

    def test_negative_price(self):
        description = {'name': 'Седло', 'brand_name': 'Mizumi',
                       'price': -1, 'email': 'test'}
        self.create_part(description, 400)
