from django.shortcuts import render
from .models import User, Submission

# Create your views here.
def home_page(request):
    users = Submission.objects.all()
    context = {'users': users}
    return render(request, 'home.html', context)