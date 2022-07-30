from django.urls import path

from .views import (
     index,
     about_us,
     estate_create,
     details_create,
     features_create,
     estate_detail,
     estate_delete,
     estate_list,
     estate_update,
     showmap,
     showroute,
     image_create, 
     image_delete,
     detail_create
)

urlpatterns = [
     path('', index, name='index'),
     path('about_us/', about_us, name='about_us'),
     path('listing/', estate_list, name="listings"),
     path('listing/add/', estate_create, name="listing_create"),
     path('listing/details/add/', details_create, name="details_create"),
     path('listing/details/features/add/', features_create, name='features_create'),
     path('listing/<int:listing_id>/', estate_detail, name="listing_detail"),
     path('listing/<int:listing_id>/delete/', estate_delete, name="listing_delete"),
     path('listing/<int:listing_id>/edit/', estate_update, name="listing_update"),
     path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>',showroute,name='showroute'),
     path('showmap/',showmap,name='showmap'),
     path('listing/images/new/<int:estate_id>', image_create, name='image_create'),  
     path('images/<image_id>/delete', image_delete, name='image_delete'),
     path('<house_id>/details/new', detail_create, name='detail_create'),   

]
