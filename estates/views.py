from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

from .forms import EstateForm, DetailsFormSet, FeaturesFormSet
from .models import Estate, Details, Features

def index(request):
	estates = Estate.objects.all()[:3]
	context = {
		'estates': estates
	}

	return render(request, 'estates/index.html', context)

def about_us(request):

	return render(request, 'estates/about_us.html', {})

def estate_list(request):
	estates = Estate.objects.all()
	context = {
		'estates': estates
	}

	return render(request, 'estates/estate_list.html', context)

@login_required
def estate_create(request):
	if request.method == 'POST':
		form = EstateForm(request.POST)
		if form.is_valid() and formset.is_valid():
			form.isntance.author = request.user
			form.save()
			return redirect('listing_list')
	else:
		form = EstateForm()

	context = {
		'form': form,
	}
	return render(request, 'estates/estate_create.html', context)

def estate_detail(request, listing_id):
	estate = Estate.objects.get(id=listing_id)
	context = {
		'estate': estate
	}
	return render(request, 'estates/estate_detail.html', context)

@login_required
def estate_delete(request, listing_id):
	estate = get_object_or_404(Estate, id=listing_id)
	if request.method == 'POST':
		estate.delete()
		return redirect('listing_list')

	context = {
		'estate': estate
	}
	return render(request, 'estates/estate_delete.html', context)

@login_required
def estate_update(request, listing_id):
	estate = get_object_or_404(Estate, id=listing_id)
	form = EstateForm(request.POST or None, instance=estate)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect('listing_list')

	context = {
		'form': form
	}

	return render(request, 'estates/estate_update.html', context)
