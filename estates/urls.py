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
    image_create, 
    image_delete
)

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('listing/', estate_list, name="listings"),
    path('listing/add/', estate_create, name="listing_create"),
    path('listing/details/add/<int:estate_id>', details_create, name="details_create"),
    path('listing/details/features/add/',
         features_create, name='features_create'),
    path('listing/<int:listing_id>/', estate_detail, name="listing_detail"),
    path('listing/<int:listing_id>/delete/',
         estate_delete, name="listing_delete"),
    path('listing/<int:listing_id>/edit/',
         estate_update, name="listing_update"),
    path('listing/images/new/<int:estate_id>', image_create, name='image_create'),  
    path('images/<image_id>/delete', image_delete, name='image_delete')
]
