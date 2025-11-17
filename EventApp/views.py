from datetime import date
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, Event,Registration
from django.utils import timezone
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Validate required fields
        if name and email and message:
            try:
                # Create and save contact
                contact = Contact(name=name, email=email, message=message)
                contact.save()
                
                # Optional: Add success message
                messages.success(request, 'Your message has been sent successfully!')
                
                return redirect('success_page')  # Redirect after successful submission
                
            except Exception as e:
                # Handle database errors
                messages.error(request, 'There was an error sending your message. Please try again.')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    # GET request - show empty form
    return render(request, 'contact.html')

def blogs(request):
     return render(request, 'blog.html')



# view to list all upcoming events
def event_list(request):
     
     # Get all events that are in the future
    # events = Event.objects.filter(Date__gte=timezone.now()).order_by('Date')
    events = Event.objects.all()
    print(f"DEBUG: Events in view: {events.count()}")
    return render(request, 'event_list.html', {'events': events})

    # events = Event.objects.all()
    # return render(request, 'event_list.html', context={'events': events})


# View for a single event's details
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_registered = False
    if request.user.is_authenticated:
        # Check if the current user is registered for this event
        is_registered = Registration.objects.filter(event=event, user=request.user).exists()
    
    context = {
        'event': event,
        'is_registered': is_registered,
    }
    
    return render(request, 'event_detail.html', context)


# View to handle event registration
@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        ticket_type = request.POST.get("ticket_type")

        if ticket_type == "regular":
            price = event.gate_fees
        else:
            price = event.gate_fees2

        # Create or get existing registration
        registration, created = Registration.objects.get_or_create(
            event=event,
            user=request.user,
            name=request.user.username,
            email=request.user.email,
            ticket_type=ticket_type,
            price=price
        )

        if created:
            event_date = event.Date.strftime("%B %d, %Y")  
            messages.success(
                request,
                f'{request.user.username}, you registered for {event.title} on {event_date}. Kindly check your email for your entry code.'
            )
        else:
            messages.info(request, "You are already registered for this event.")

        return redirect('event_detail', event_id=event.id)

    return redirect('event_detail', event_id=event.id)





@login_required
def cancel_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        # Find and delete the registration
        Registration.objects.filter(event=event, user=request.user).delete()
        # You can add a success message here
        return redirect('event_detail', event_id=event.id)
    # Redirect if not a POST request
    return redirect('event_detail', event_id=event.id)


# View for the user to see their own registrations
@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user).order_by('event__Date')
    return render(request, 'register_event.html', {'registrations': registrations})


def event_register_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        discription = request.POST["discript"]
        date = request.POST["date"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        location = request.POST["locate"]
        regular = request.POST["regular"]
        vip = request.POST["vip"]
        image = request.FILES.get("image")

        eventForm = Event(title=name, Description=discription, Date=date,
        start_time=start_time,
        end_time=end_time, Location=location,gate_fees=regular,gate_fees2=vip, image=image)
        eventForm.save()
        return redirect('event_list')
    else:
        return render(request,'event_register_form.html')

# def register_event(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             registration = form.save(commit=False)
#             registration.event = event
#             registration.save()
#             return redirect('event_list')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register_event.html', {'form': form, 'event': event})
