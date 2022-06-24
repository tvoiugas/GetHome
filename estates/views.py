from django.shortcuts import render

from .models import Estate

def index(request):
	estates = Estate.objects.all()[:5]
	context = {
		'estates': estates
	}

	return render(request, 'estates/index.html', context)
