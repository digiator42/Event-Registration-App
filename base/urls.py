from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('account', views.account, name='account'),
    path('events', views.events, name='events'),
    path('submission/<str:pk>', views.submission_page, name='submission-page'),
    path('update-submission/<str:pk>', views.update_submission, name='update-submission'),
    path('event/<str:pk>', views.event, name='event'),
    path('event-confirmation/<str:pk>', views.event_confirmation, name='event-confirmation'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('create-submission/<str:pk>', views.create_submission, name='create-submission'),
]