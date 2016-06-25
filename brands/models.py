# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.db.models import Count


class BikeBrandManager(models.Manager):

    def get_popular(self):
        # Получение статистики по популярным маркам деталей.
        # Выводятся марки, детали которых встречаются чаще 5 раз.
        # Результат отсортирован по количеству деталей марки.
        aggregated = self.get_queryset().annotate(parts_qty=Count('bikepart'))
        return aggregated.filter(parts_qty__gt=5).order_by('-parts_qty')


class BikeBrand(models.Model):

    name = models.CharField(max_length=100)

    objects = BikeBrandManager()

    def __unicode__(self):
        return self.name
