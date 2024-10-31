from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import RecordForm
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
    messages.success(request, "Welcome " + request.user.first_name)
    records = Record.objects.filter(user=request.user)
    return render(request, 'loggedIn.html', {'records':records})

@login_required
def addRecord(request):
    if request == "POST":
        form = RecordForm(request.POST or None)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user # logged-in user's record here
            record.save()
            messages.success(request, 'Record saved successfully!')
        else:
            messages.success(request, "Error, Please try again.")
    else:
        form = RecordForm
    return render(request, 'addRecord.html', {'form':form})

def logout_user(request):
    logout(request)
    return render(request, 'home.html', {})