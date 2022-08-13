from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .models import Estate
from functools import wraps

def check_author(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        listing_id = kwargs['listing_id']
        estate = Estate.objects.get(id=listing_id)
        
        if request.user == estate.author:
            return view_func(request, *args, **kwargs)

        else:
            html="<html><body>Вы не автор объявления.</body></html>"
            return redirect('listings')
    return wrapper