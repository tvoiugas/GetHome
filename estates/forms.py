from django import forms
from django.forms import inlineformset_factory
from estates.models import Estate, Details, Feature, Tag, EstateImage


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = (
            'title', 'price', 'area',
            'estate_type', 'location',
            'video', 'description'
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


# FeaturesFormSet = inlineformset_factory(
#     Estate, Feature, form=FeaturesForm, extra=4)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class ImageForm(forms.ModelForm):
    class Meta:
        model = EstateImage
        fields = ('file',)