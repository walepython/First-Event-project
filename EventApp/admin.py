from .models import Contact, Event,Registration
from django.contrib import admin

# Register your models here.
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Contact)
