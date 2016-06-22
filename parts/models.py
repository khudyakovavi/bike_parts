# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.db.models import Count


class BikeBrandManager(models.Manager):

    def get_popular(self):
        aggregated = self.get_queryset().annotate(parts_qty=Count('bikepart'))
        return aggregated.filter(parts_qty__gt=5).order_by('-parts_qty')


class BikeBrand(models.Model):

    name = models.CharField(max_length=100)

    objects = BikeBrandManager()

    def __unicode__(self):
        return self.name


class BikePart(models.Model):

    name = models.CharField(max_length=256)
    brand = models.ForeignKey(BikeBrand)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    contacts = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.brand, self.name)
