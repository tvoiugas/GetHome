from django.urls import path

from .views import index, estate_create, estate_detail, estate_delete, estate_list, estate_update

urlpatterns = [
	path('', index, name = 'index'),
	path('estate_list', estate_list, name = "estate_list"),
	path('estate_create', estate_create, name = "estate_create"),
	path('estate_detail', estate_detail, name = "estate_detail"),
	path('estate_delete', estate_delete, name = "estate_delete"),
	path('estate_update', estate_update, name = "estate_update"),
]