import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eventproject.settings')
django.setup()

from EventApp.models import Event

print("=== EVENT FIELD CHECK ===")
events = Event.objects.all()
for event in events:
    print(f"\nEvent: '{event.title}' (ID: {event.id})")
    
    # Check common boolean fields
    if hasattr(event, 'is_available'):
        print(f"  is_available: {event.is_available}")
    else:
        print("  No is_available field")
        
    if hasattr(event, 'is_active'):
        print(f"  is_active: {event.is_active}")
    else:
        print("  No is_active field")
        
    if hasattr(event, 'status'):
        print(f"  status: {event.status}")
    else:
        print("  No status field")

print(f"\nTotal events: {events.count()}")
