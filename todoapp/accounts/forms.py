from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput())
    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True, error_messages={'required': 'please enter your first name'})
    last_name = forms.CharField(max_length=200, required=True)
    username = forms.CharField(max_length=200, required=True)
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    password1 = forms.CharField(widget = forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])
    password2 = forms.CharField(widget = forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])
    
    class Meta:
        model = User
        fields = {'first_name','last_name', 'username', 'password1', 'password2', 'email'}
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()

class RecoverForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    
    