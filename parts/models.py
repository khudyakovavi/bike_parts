# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from brands.models import BikeBrand


class BikePartManager(models.Manager):

    def create(self, **kwargs):
        brand_name = kwargs.get('brand_name')
        brand = BikeBrand.objects.filter(name=brand_name).first()
        if brand is None:
            brand = BikeBrand(name=brand_name)
            brand.save()
        contacts = [kwargs.get('phone'), kwargs.get('email')]
        if all(contacts):
            contacts = ', '.join(contacts)
        else:
            contacts = contacts[0] or contacts[1]
        return super(BikePartManager, self).create(
            name=kwargs.get('name'),
            brand=brand,
            price=kwargs.get('price'),
            contacts=contacts
        )


class BikePart(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название детали')
    brand = models.ForeignKey(BikeBrand, verbose_name='Марка')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8,
                                verbose_name='Цена')
    contacts = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    objects = BikePartManager()

    def __unicode__(self):
        return '{0}: {1}'.format(self.brand, self.name)
