# coding: utf-8
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic import View, TemplateView

from parts.utils import BikePartUtils


class MainView(TemplateView):

    template_name = 'parts.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        page = self.request.GET.get('page')
        context['bike_parts'] = BikePartUtils.get_bike_parts_page(page)
        return context


class BikePartAdView(View):

    def get(self, request, *args, **kwargs):
        fields = ['name', 'brand', 'price', 'contacts']
        page = request.GET.get('page')
        parts = [
            model_to_dict(part, fields=fields)
            for part in BikePartUtils.get_bike_parts_page(page)
        ]
        return JsonResponse({'parts': parts})
