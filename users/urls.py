from django.urls import path
from .views import login_page, logout_page, register_page, profile_page


urlpatterns = [
    path('login_page', login_page, name='login_page'),
    path('logout_page', logout_page, name='logout_page'),
    path('register_page', register_page, name='register_page'),
    path('profile/<int:userID>', profile_page, name='profile'),
    path('activate/<uidb64>/<token>', profile_page, name='activation'),
]
