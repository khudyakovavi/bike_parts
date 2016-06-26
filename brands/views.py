# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView

from .models import BikeBrand


class PopularBrandsView(TemplateView):

    template_name = 'brands.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PopularBrandsView, self).get_context_data(**kwargs)

        context['bike_brands'] = BikeBrand.objects.get_popular()
        return context
