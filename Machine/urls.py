from Machine.models import Profile
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='Homepage'),
    path('home', views.home, name='home'),
    path('Appearence', views.Appearence, name='Appearence'),
    path('Performs', views.Performs, name='Performs'),
    path('Publicity', views.Publicity, name='Publicity'),
    path('results', views.results, name='results'),
    path('Profile', views.profile, name='Profile'),
    path('Profile2', views.profile2, name='Profile2'),
    path('Bookings', views.Bookings, name='Bookings'),
    path('Artist', views.Artist, name='Artist'),
    path('About_us', views.About_us, name='About Us'),
    path('Artist_Page', views.Artist_Page, name='Artist Page'),
    path('email', views.email, name='email')
]

