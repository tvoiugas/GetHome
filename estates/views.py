from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import EstateForm, DetailsForm, FeaturesForm, FeaturesFormSet
from .models import Estate, Details, Feature
from .filters import EstateFilter


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['HX-Redirect']=self['Location']
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
	if request.GET:
		sort=request.GET.get('sort', 'price')
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
		initial = {
			'title': request.session.get('title', None),
			'estate_type': request.session.get('estate_type', None),
			'description': request.session.get('description', None),
			'location': request.session.get('location', None),
			'price': request.session.get('price', None),
			'area': request.session.get('area', None),
			'photo': request.session.get('photo', None),
			'video': request.session.get('video', None)
		}
		form = EstateForm(request.POST, request.FILES, initial = initial)
		if form.is_valid():
			request.session['title'] = form.cleaned_data['title']
			request.session['estate_type'] = form.cleaned_data['estate_type']
			request.session['description'] = form.cleaned_data['description']
			request.session['location'] = form.cleaned_data['location']
			request.session['price'] = form.cleaned_data['price']
			request.session['area'] = form.cleaned_data['area']
			request.session['photo'] = form.cleaned_data['photo']
			request.session['video'] = form.cleaned_data['video']
			return HttpResponse(status = 204)
		else:
			for field in form:
				for error in field.errors:
					print(error, field)
	context = {
		'form': form,
	}
	return render(request, 'estates/estate_create.html', context)

def details_create(request):
	form = DetailsForm()

	if request.method == "POST":
		initial = {
			'bathrooms': request.session.get('bathrooms', None),
			'bedrooms': request.session.get('bedrooms', None),
			'garages': request.session.get('garages', None),
			'floors': request.session.get('floors', None),	
			'floor_on': request.session.get('floor_on', None)
		}
		form = DetailsForm(request.POST, initial = initial)
		if form.is_valid():
			request.session['bathrooms'] = form.cleaned_data['bathrooms']
			request.session['bedrooms'] = form.cleaned_data['bedrooms']
			request.session['garages'] = form.cleaned_data['garages']
			request.session['floors'] = form.cleaned_data['floors']
			request.session['floor_on'] = form.cleaned_data['floor_on']
			return HttpResponse(status = 204)

	context = {
		'form': form,
	}

	return render(request, 'estates/details_create.html', context)

def features_create(request):
	formset = FeaturesFormSet()

	if request.method == "POST":
		formset = FeaturesFormSet(request.POST, request.FILES)
		if formset.is_valid():
			estate = Estate.objects.create(
				title = request.session['title'],
				estate_type = request.session['estate_type'],
				description = request.session['description'],
				location = request.session['location'],
				price = request.session['price'],
				area = request.session['area'],
				photo = '/estate_photos/' + request.session['photo'],
				video = request.session['video'],
				author = request.user
			)
			formset = FeaturesFormSet(request.POST, instance = estate)
			detail = Details.objects.create(
				bathrooms = request.session['bathrooms'],
				bedrooms = request.session['bedrooms'],
				garages = request.session['garages'],
				floors = request.session['floors'],
				floor_on = request.session['floor_on'],
				estate = estate,
			)
			for form in formset:
				form.save()
			return HTTPResponseHXRedirect(reverse('listings'))

	context = {
		'formset': formset
	}

	return render(request, 'estates/features_create.html', context)

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