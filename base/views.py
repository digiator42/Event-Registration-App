from django.shortcuts import render, redirect
from .models import User, Submission, Event
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, SubmissionForm
from django.contrib.auth import login, logout
from typing import Dict
from django.contrib.auth.decorators import login_required


# Create your views here.
def _spa_content(request, template: str, context: Dict):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('------> ', template)
        return render(request, template, context)

    context['block_content'] = template
    return render(request, 'base.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            context = {'form': form, 'page': 'login'}
    else:
        form = AuthenticationForm()
        context = {'form': form, 'page': 'login'}
    return _spa_content(request, 'login_register.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            context = {'form': form, 'page': 'register'}
    else:
        form = CustomUserCreationForm()
        context = {'form': form, 'page': 'register'}
    return _spa_content(request, 'login_register.html', context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_page(request):
    subs = Submission.objects.exclude(participant__username='admin')
    events = Event.objects.all()
    context = {'subs': subs, 'events': events}

    return _spa_content(request, 'home.html', context)

@login_required(login_url='login')
def event(request, pk):
    event = Event.objects.get(id=pk)
    submitted = Submission.objects.filter(participant=request.user, event=event).exists()
    context = {'event': event, 'submitted': submitted}
    return _spa_content(request, 'event.html', context)

@login_required(login_url='login')
def events(request):
    events = Event.objects.all()
    context = {'events': events}
    return _spa_content(request, 'events.html', context)

@login_required(login_url='login')
def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    
    context = {'event': event}
    return _spa_content(request, 'event_confirmation.html', context)

@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    user_events = Event.objects.filter(participants=request.user)
    context = {'events': user_events, 'user': user}
    return _spa_content(request, 'profile.html', context)

@login_required(login_url='login')
def account(request):
    user_events = Event.objects.filter(participants=request.user)
    context = {'events': user_events}
    return _spa_content(request, 'account.html', context)

@login_required(login_url='login')
def create_submission(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant = request.user
            submission.event = event
            submission.save()
            return redirect('home')
    else:
        form = SubmissionForm()
    
    context = {'form': form, 'event': event}
    return _spa_content(request, 'create_submission.html', context)

@login_required(login_url='login')
def submission_page(request, pk):
    submission = Submission.objects.get(id=pk)
    context = {'submission': submission}
    return _spa_content(request, 'submission.html', context)

@login_required(login_url='login')
def update_submission(request, pk):
    submission = Submission.objects.get(id=pk)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = SubmissionForm(instance=submission)
    
    context = {'form': form, 'submission': submission}
    return _spa_content(request, 'update_submission.html', context)