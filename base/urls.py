from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('event/<str:pk>', views.event, name='event'),
    path('event-confirmation/<str:pk>', views.event_confirmation, name='event-confirmation'),
    path('profile/<str:pk>', views.profile, name='profile'),
]