from django import forms
from django.forms import inlineformset_factory
from estates.models import Estate, Details, Feature, Tag, HouseImage


class EstateForm(forms.ModelForm):
    latitude = forms.CharField(widget=forms.HiddenInput())
    longitude = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Estate
        fields = (
            'title', 'price', 'area',
            'estate_type', 'location',
            'video', 'description',
            'tags', 'latitude', 'longitude'
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

class ImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ('file',)

# FeaturesFormSet = inlineformset_factory(
#     Estate, Feature, HouseImage, ImageForm, form=FeaturesForm, extra=4)


