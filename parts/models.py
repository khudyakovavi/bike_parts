# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class BikePart(models.Model):

    name = models.CharField(max_length=256)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    contacts = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
