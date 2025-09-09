# events/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# We are creating a new form that inherits from UserCreationForm
class RegistrationForm(UserCreationForm):
    # Add an email field, which is required
    email = forms.EmailField(required=True)

    class Meta:
        # We are using the default User model
        model = User
        # These are the fields that will be displayed on the form
        # 'password2' is the confirmation field
        fields = ("username", "email", "password", "password2")

    def save(self, commit=True):
        # Save the user object
        user = super(RegistrationForm, self).save(commit=False)
        # Set the email from the cleaned form data
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user