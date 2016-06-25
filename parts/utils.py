# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import BikePart


class BikePartUtils(object):

    @staticmethod
    def get_bike_parts_page(page):
        bike_parts = BikePart.objects.order_by('created')
        parts_paginator = Paginator(bike_parts, 10)
        try:
            parts = parts_paginator.page(page)
        except PageNotAnInteger:
            parts = parts_paginator.page(1)
        except EmptyPage:
            parts = parts_paginator.page(parts_paginator.num_pages)
        return parts
