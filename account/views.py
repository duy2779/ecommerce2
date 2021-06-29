from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .form import RegistrationForm

# Create your views here.


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration success')
            return redirect('account:register')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('account:login')
        messages.error(request, 'Username or password is incorrect')
    return render(request, 'account/login.html')


def log_out(request):
    logout(request)
    return redirect('account:login')