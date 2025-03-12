from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, blank=True)
    picture = models.ImageField(default='default.png')
    bio = models.TextField(max_length=200, blank=True)
    
    # Login with email instead of username
    USERNAME_FIELD = 'email'
    # Username is email and email must be unique if it's required
    REQUIRED_FIELDS = ['username']
    
class Event(models.Model):
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User, blank=True, related_name='events')
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, default='Egypt')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='submissions')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    details = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.event) + '---' + str(self.participant)
    