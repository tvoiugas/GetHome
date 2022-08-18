from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import EstateForm, DetailsForm, FeaturesForm, ImageForm, HouseImage
from .models import Estate, Details, Feature
from .filters import EstateFilter
from .decorators import check_author
from django.contrib import messages
from django.core.paginator import Paginator


class HTTPResponseHXRedirect(HttpResponseRedirect):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self['HX-Redirect'] = self['Location']
	status_code = 200


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
	f=EstateFilter(request.GET, queryset=Estate.objects.all())
	sort=request.GET.get('sort')
	if sort:
		f = EstateFilter(request.GET, queryset=Estate.objects.all().order_by(sort))
	
	context = {
		'estates': estates,
		'f': f,
	}

	return render(request, 'estates/estate_list.html', context)

@login_required
def estate_create(request):
	form = EstateForm(request.POST or None, request.FILES)
	if request.method == "POST":
		if form.is_valid():
			estate = form.save(commit=False)
			estate.author = request.user
			estate.save()
			detail_form = DetailsForm()
			detail_context = {'detail_form': detail_form, 'estate_id': estate.pk}
			return render(request, 'estates/details_create.html', detail_context)
	context = {
		'form': form,
	}
	return render(request, 'estates/estate_create.html', context)

@login_required
def details_create(request, estate_id):
	detail_form = DetailsForm(request.POST or None)
	estate = get_object_or_404(Estate, pk=estate_id)
	if request.method == "POST":
		if detail_form.is_valid():
			detail_obj = detail_form.save(commit=False)
			detail_obj.estate = estate
			detail_obj.save()
			image_form = ImageForm()
			image_context = {'image_form': image_form, 'estate_id': estate.pk}
			return render(request, 'estates/image_create.html', image_context)
	context = {'detail_form': detail_form, 'estate_id': estate.pk}

	return render(request, 'estates/details_create.html', context)

@login_required
def features_create(request, estate_id):
	estate = get_object_or_404(Estate, pk=estate_id)

		
	context = {
	
		
	}
	
	return render(request, 'estates/features_create.html', context)
	
@login_required
def image_create(request, estate_id):
	estate = get_object_or_404(Estate, pk=estate_id)
	form = ImageForm()
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			img = form.save(commit=False)
			img.house = estate
			img.save()
			return render(request, 'estates/image_template.html', {'image': img})
	context = {'image_form': form, 'estate_id': estate.pk}
	return render(request, 'estates/image_form.html', context)

def estate_detail(request, listing_id):
	estate = Estate.objects.get(id=listing_id)
	estate_images = estate.images.all()[1:]
	print(estate_images)
	context = {
		'estate': estate,
		'estate_images': estate_images
	}
	return render(request, 'estates/estate_detail.html', context)


@login_required
@check_author
def estate_delete(request, listing_id):
	estate = get_object_or_404(Estate, id=listing_id)
	if request.method == 'POST':
		estate.delete()
		return redirect('listings')
	context = {
		'estate': estate
	}
	return render(request, 'estates/estate_delete.html', context)


@login_required
@check_author
def estate_update(request, listing_id):
	estate = get_object_or_404(Estate, id=listing_id)
	form = EstateForm(request.POST or None, instance=estate)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('listing_list')
	
	context = {
		'form': form
	}

	return render(request, 'estates/estate_update.html', context)

@login_required
def image_delete(request, image_id):
	img = get_object_or_404(HouseImage, pk=image_id)
	img.delete()
	return HttpResponse('')
