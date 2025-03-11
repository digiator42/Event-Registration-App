from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('event/<str:pk>', views.event, name='event'),
    path('event-confirmation/<str:pk>', views.event_confirmation, name='event-confirmation'),
    path('profile/<str:pk>', views.profile, name='profile'),
]