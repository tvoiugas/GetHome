from django import forms

from estates.models import Estate, Details, Feature, Tag

class EstateForm(forms.ModelForm):
	class Meta:
		model = Estate
		fields = (
			'title', 'estate_type', 'description',
			'location', 'price', 'area',
			'photo', 'video'
		)


class DetailsForm(forms.ModelForm):
	class Meta:
		model = Details
		fields = (
			'bathrooms', 'bedrooms', 'garages',
			'floors', 'floor_on'
		)


class FeaturesForm(forms.ModelForm):
	class Meta:
		model = Feature
		fields = (
			'kind',
		)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'name',
        )