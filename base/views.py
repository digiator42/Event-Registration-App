from django.shortcuts import render, redirect
from .models import User, Submission, Event
from django.http import JsonResponse

# Create your views here.
def spa_content(request, template, context):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, template, context)
    
    context['block_content'] = template
    return render(request, 'base.html', context)

def home_page(request):
    users = Submission.objects.all()
    events = Event.objects.all()
    context = {'users': users, 'events': events}

    return spa_content(request, 'home.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return spa_content(request, 'event.html', context)

def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    
    context = {'event': event}
    return spa_content(request, 'event_confirmation.html', context)

def profile(request, pk):
    user_events = Event.objects.filter(participants=request.user)
    context = {'events': user_events}
    return spa_content(request, 'profile.html', context)