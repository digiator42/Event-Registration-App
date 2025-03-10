from django.shortcuts import render, redirect
from .models import User, Submission, Event
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from typing import Dict

# Create your views here.
def _spa_content(request, template: str, context: Dict):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('------> ', template)
        return render(request, template, context)

    context['block_content'] = template
    return render(request, 'base.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return _spa_content(request, 'login_register.html', {'form': form})

def register_view(request):
    pass

def logout_view(request):
    logout(request)
    return redirect('login')

def home_page(request):
    users = Submission.objects.all()
    events = Event.objects.all()
    context = {'users': users, 'events': events}

    return _spa_content(request, 'home.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return _spa_content(request, 'event.html', context)

def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    
    context = {'event': event}
    return _spa_content(request, 'event_confirmation.html', context)

def profile(request, pk):
    user_events = Event.objects.filter(participants=request.user)
    context = {'events': user_events}
    return _spa_content(request, 'profile.html', context)