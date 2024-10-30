from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loggedIn')
        else:
            messages.success(request, "Error, Please try again.")
    return render(request, 'home.html', {})


@login_required
def loggedIn(request):
    return render(request, 'loggedIn.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'home.html', {})