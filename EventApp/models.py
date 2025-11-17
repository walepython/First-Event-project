from django.db import models
from datetime import time
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
       title = models.CharField(max_length=225, null=True, blank=True)
       Description = models.TextField()
       Date = models.DateTimeField()
       start_time = models.TimeField(null=True, blank=True, default=None)
       end_time = models.TimeField(null=True, blank=True, default=None)
       Location = models.CharField(max_length=225)
       image = models.ImageField(upload_to='picture', null=True, blank=True)
       gate_fees = models.IntegerField(null=True, blank=True, default=None)
       gate_fees2 = models.IntegerField(null=True, blank=True, default=None)

       def __str__(self):
              return self.title if self.title else "Untitled Event"
       
class Registration(models.Model):
       TICKET_CHOICES = [
        ('regular', 'Regular'),
        ('vip', 'VIP'),
    ]
       event = models.ForeignKey(Event, on_delete=models.CASCADE)
       user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
       name = models.CharField(max_length=225)
       email = models.EmailField()
       ticket_type = models.CharField(max_length=10, choices=TICKET_CHOICES, default='regular')
       price = models.IntegerField(null=True, blank=True)
       timestamp = models.DateTimeField(auto_now_add=True)


       class Meta:
        # This ensures that a user can only register for an event once
        unique_together = ('event', 'user','ticket_type')
       
       def __str__(self):
        return f'{self.user.username} registered for {self.event.title} ({self.ticket_type})'
       
class Contact(models.Model):
     name = models.CharField(max_length=20,null=True)
     email = models.EmailField()
     message = models.TextField(max_length=220,null=True)

     def __str__(self):
          return self.name