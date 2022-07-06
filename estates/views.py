from django.shortcuts import render, get_object_or_404, redirect
from .forms import EstateForm
from .models import Estate

def index(request):
	estates = Estate.objects.all()[:3]
	context = {
		'estates': estates
	}

	return render(request, 'estates/index.html', context)


def estate_list(request):
	estates = Estate.objects.all()
	context = {
		'estates': estates
	}

	return render(request, 'estates/estate_list.html', context)


def estate_create(request):
	form = EstateForm()
	if request.method == 'POST':
		form = EstateForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('estate_list')

	context = {
		'form': form
	}
	return render(request, 'estates/estate_create.html', context)


def estate_detail(request, estate_id):
	estate = Estate.objects.get(id=estate_id)
	context = {
		'estate': estate
	}
	return render(request, 'estates/estate_detail.html', context)


def estate_delete(request, estate_id):
	estate = get_object_or_404(Estate, id=estate_id)
	if request.method == 'POST':
		estate.delete()
		return redirect('estate_list')

	context = {
		'estate': estate
	}
	return render(request, 'estate/estate_delete.html', context)


def estate_update(request, estate_id):
	estate = get_object_or_404(Estate, id=estate_id)
	form = EstateForm(request.POST or None, instance=estate)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect('estate_list')

	context = {
		'form': form
	}
	return render(request, 'estate/estate_update.html', context)