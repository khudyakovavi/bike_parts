# coding: utf-8
from __future__ import absolute_import

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from common.constants import PAGE_SIZE


class BikePartUtils(object):

    @staticmethod
    def get_bike_parts_page(bike_parts, page):
        parts_paginator = Paginator(bike_parts, PAGE_SIZE)
        try:
            parts = parts_paginator.page(page)
        except PageNotAnInteger:
            parts = parts_paginator.page(1)
        except EmptyPage:
            parts = parts_paginator.page(parts_paginator.num_pages)
        return parts
