from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginForm, SignUpForm, RecoverForm, SetNewPasswordForm
from django.views.decorators.csrf import csrf_exempt

def login_view(request):
    context = {}
    context['form'] = LoginForm()
    return render(request, 'login.html', context)

@csrf_exempt
def signup_view(request):
    context = {}
    form = SignUpForm(request.POST)
    context['form'] = form
    if request.method == "POST":

        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    

    
    return render(request, 'signup.html', context)

@csrf_exempt
def password_reset_view(request):
    context = {}
    form = RecoverForm(request.POST)
    context['form'] = form
    
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            form.save(from_email='blabla@blabla.com', request=request)
            return redirect('login')
    return render(request, 'registration/password_reset_form.html', context)
    
@csrf_exempt
def password_set_view(request):
    context = {}
    form = SetNewPasswordForm(request.POST or None)
    context["form"] = form
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'password_reset_form.html', context)