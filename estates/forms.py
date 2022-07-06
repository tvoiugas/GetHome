from django import forms
from estates.models import Estate

class EstateForm(forms.ModelForm):
	class Meta:
		model = Estate
		fields = (
			'title', 'estate_type', 'slug', 'description', 'location', 'author', 'price', 'area'
		)