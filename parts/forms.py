# coding: utf-8
from __future__ import unicode_literals

from django import forms

from .models import BikePart


class BikePartForm(forms.ModelForm):

    brand_name = forms.CharField(required=True, max_length=100, label='Марка')
    price = forms.DecimalField(min_value=0, initial=0, decimal_places=2,
                               max_digits=8, label='Цена', required=True)
    phone = forms.CharField(required=False, max_length=12, label='Телефон')
    email = forms.EmailField(required=False, max_length=86)

    def clean(self):
        cleaned_data = super(BikePartForm, self).clean()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')

        if not phone and not email:
            raise forms.ValidationError('Должно быть заполнено хотя '
                                        'бы одно поле с контактами.')

        return cleaned_data

    class Meta:
        model = BikePart
        fields = ('name', 'brand_name', 'price', 'phone', 'email')
