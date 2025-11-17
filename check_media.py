import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eventproject.settings')
django.setup()

from EventApp.models import Event

print("=== MISSING MEDIA CHECK ===")
events = Event.objects.all()
for event in events:
    print(f"\nEvent: '{event.title}'")
    
    # Check image field (common field names)
    image_fields = ['image', 'picture', 'photo', 'banner', 'thumbnail']
    for field_name in image_fields:
        if hasattr(event, field_name):
            image_field = getattr(event, field_name)
            if image_field:
                print(f"  {field_name}: {image_field.name}")
                # Check if file exists
                if image_field and hasattr(image_field, 'path'):
                    if os.path.exists(image_field.path):
                        print(f"    ✅ File exists: {image_field.path}")
                    else:
                        print(f"    ❌ File missing: {image_field.path}")
            else:
                print(f"  {field_name}: No image set")

print("\nCheck complete")
