
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .form import RegistrationForm # Import our new form

# Create your views here.





def register(request):
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = RegistrationForm(request.POST)
        # Check if the form is valid (e.g., passwords match, username isn't taken)
        if form.is_valid():
            # Save the new user to the database
            form.save()
            username = form.cleaned_data.get('username')
            # Send a success message to the user
            messages.success(request, f'Account created for {username}! You can now log in.')
            # Redirect them to the login page
            return redirect('login')
    # If it's a GET request, just create a blank form
    else:
        form = RegistrationForm()
    
    # Render the template with the form
    return render(request, 'register_form.html', {'form': form})



def login(request):
    if request.method == "POST":
        # Get the 'next' parameter from the form's action URL or from the POST data
        next_url = request.POST.get('next', request.GET.get('next'))
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            
            # If a 'next' URL was provided and it's safe, redirect there
            if next_url:
                return redirect(next_url)
            else:
                # Otherwise, redirect to the default event list
                return redirect("event_list")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request,"logout.html")

