from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginForm, SignUpForm
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