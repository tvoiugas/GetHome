from django import forms
from django.forms import BaseModelFormSet
from django.forms import inlineformset_factory

from estates.models import Estate, Details, Features

class EstateForm(forms.ModelForm):
	class Meta:
		model = Estate
		fields = (
			'title', 'estate_type', 'description',
			'location', 'price', 'area',
			'photo', 'video'
		)


class DetailForm(forms.ModelForm):
	class Meta:
		model = Details
		fields = (
			'bathrooms', 'bedrooms', 'garages',
			'floors', 'floor_on'
		)


class FeaturesForm(forms.ModelForm):
	class Meta:
		model = Features
		fields = (
			'kind',
		)



DetailsFormSet = inlineformset_factory(Estate, Details, form = DetailForm)
FeaturesFormSet = inlineformset_factory(Estate, Features, form = FeaturesForm)