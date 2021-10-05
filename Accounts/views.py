from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User Created')
    else:
        form = CreateUserForm()
    return render(request, 'Register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.Info('There Was An Error Logging In Try Again')
            return redirect('login_user')
    else:
        return render(request, "Login.html", {})
