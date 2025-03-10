from django.shortcuts import render, redirect
from .models import User, Submission, Event

# Create your views here.
def home_page(request):
    users = Submission.objects.all()
    events = Event.objects.all()
    context = {'users': users, 'events': events}
    return render(request, 'home.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'event.html', context)

def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    context = {'event': event}
    return render(request, 'event_confirmation.html', context)

def profile(request, pk):
    user_events = Event.objects.filter(participants=request.user)
    context = {'events': user_events}
    return render(request, 'profile.html', context)