# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView

from parts.forms import BikePartForm
from .models import BikePart
from .utils import BikePartUtils


class BikePartListView(TemplateView):

    template_name = 'parts.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BikePartListView, self).get_context_data(**kwargs)

        page = self.request.GET.get('page')
        search = self.request.GET.get('search')

        bike_parts = BikePart.objects.order_by('-created')
        bike_parts = bike_parts.prefetch_related('brand')
        if search:
            bike_parts = bike_parts.filter(
                Q(name__icontains=search) | Q(brand__name__icontains=search)
            )

        context['bike_parts'] = BikePartUtils.get_bike_parts_page(
            bike_parts, page
        )
        return context


class BikePartView(FormView):

    template_name = 'new_part.html'
    form_class = BikePartForm
    success_url = '/'

    def form_valid(self, form):
        part = BikePart.objects.create(**form.cleaned_data)
        part.save()
        return HttpResponseRedirect('/')
