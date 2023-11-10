from django import forms
from django.contrib.auth.models import User


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")


class CrispyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CrispyAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login')
        )


class CrispyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CrispyUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            Submit('submit', 'Register')
        )
