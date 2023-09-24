from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'user/registration.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'user/login.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'user/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))