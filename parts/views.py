# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView

from .utils import BikePartUtils


class MainView(TemplateView):

    template_name = 'parts.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        page = self.request.GET.get('page')
        context['bike_parts'] = BikePartUtils.get_bike_parts_page(page)
        return context
