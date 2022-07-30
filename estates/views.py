from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import folium
from . import getroute
from .forms import EstateForm, DetailsForm, ImageForm, FeaturesForm #FeaturesFormSet
from .models import Estate, Details, Feature, EstateImage
from .filters import EstateFilter
from .decorators import check_author
from django.contrib import messages

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
	f=EstateFilter(request.POST, queryset=Estate.objects.all())
	sort=request.POST.get('sort')
	if sort:
		f = EstateFilter(request.POST, queryset=Estate.objects.all().order_by(sort))
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


def features_create(request, estate_id):
    # formset = FeaturesFormSet()
    estate = get_object_or_404(Estate, pk=estate_id)
    
    context = {
        'formset': formset,
		
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
@check_author
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

def showmap(request):
    return render(request,'estates/showmap.html')

def showroute(request,lat1,long1,lat2,long2):
    figure = folium.Figure()
    lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)
    route=getroute.get_route(long1,lat1,long2,lat2)
    m = folium.Map(location=[(route['start_point'][0]), (route['start_point'][1])], zoom_start=10)
    m.add_to(figure)
    folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
    folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
    folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
    figure.render()
    context={'map':figure}
    return render(request,'estates/showroute.html',context)


@login_required
def image_create(request, estate_id):
    estate = get_object_or_404(Estate, pk=estate_id)
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.estate = estate
            img.save()
            return render(request, 'estates/partials/image_template.html', {'image': img})
    context = {'image_form': form, 'estate_id': estate.pk}
    return render(request, 'estates/partials/image_form.html', context)


@login_required
def image_delete(request, image_id):
    img = get_object_or_404(EstateImage, pk=image_id)
    img.delete()
    return HttpResponse('')

@login_required
def detail_create(request, estate_id):
    estate = get_object_or_404(estate, pk=estate_id)
    form = DetailsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            detail_obj = form.save(commit=False)
            detail_obj.estate = estate
            detail_obj.save()
            image_form = ImageForm()
            image_context = {'image_form': image_form, 'estate_id': estate.pk}
            return render(request, 'estate/partials/image_create.html', image_context)
    context = {'form': form, 'estate_id': estate.pk}
    return render(request, 'estate/partials/detail_create.html', context)

