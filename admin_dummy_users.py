import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_registration.settings')
django.setup()


from base.models import User, Event, Submission
from faker import Faker
from django.core.management import call_command
# Flush the database
call_command('flush', '--no-input')

fake = Faker()

# superuser
superuser = User.objects.create_superuser(
    username='admin',
    email='admin@admin.com',
    password='adminpassword'
)
superuser.first_name = 'Admin'
superuser.last_name = 'User'
superuser.save()

# dummy users
for _ in range(10):
    user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='dummypassword'
    )
    user.first_name = fake.first_name()
    user.last_name = fake.last_name()
    user.bio = fake.text()
    user.save()

# events
for _ in range(4):
    event = Event.objects.create(
        name='Fake Hackathon' + ' | ' + '2025',
        description=fake.text(),
        location=fake.city(),
        start_date=fake.future_datetime(),
        end_date=fake.future_datetime(end_date='+30d'),
        registration_deadline=fake.future_datetime(end_date='+10d')
    )
    event.participants.set(User.objects.order_by('?')[:5])
    event.save()
    
# submissions
for _ in range(10):
    submission = Submission.objects.create(
        participant=User.objects.order_by('?').first(),
        event=Event.objects.order_by('?').first(),
        details=fake.text()
    )
    submission.save()

print("Superuser and dummy users created successfully.")