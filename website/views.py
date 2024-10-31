from django.shortcuts import render, redirect, get_object_or_404
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
            messages.error(request, "Error, Please try again.")
    return render(request, 'home.html', {})


@login_required
def loggedIn(request):
    messages.success(request, "Welcome " + request.user.first_name)
    records = Record.objects.filter(user=request.user)
    return render(request, 'loggedIn.html', {'records':records})

@login_required
def addRecord(request):
    if request.method == "POST":
        form = RecordForm(request.POST or None)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user # logged-in user's record here
            record.save()
            messages.success(request, 'Record saved successfully!')
        else:
            messages.error(request, "Error, Please try again.")
    else:
        form = RecordForm
    return render(request, 'addRecord.html', {'form':form})

@login_required
def single_record(request, record_id):
    record = get_object_or_404(Record, id=record_id) #will be returning 404 if record not found
    return render(request, 'singleRecord.html', {'record':record})


@login_required
def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == "POST":
        record.delete()
        return redirect('loggedIn')

@login_required
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, 'Record updated successfully!')
            return redirect('loggedIn')
        else:
            messages.error(request, "Error, Please try again.")
    else:
        form = RecordForm(instance=record)
    return render(request, 'updateRecord.html', {'form':form, 'record':record})
    

def logout_user(request):
    logout(request)
    return render(request, 'home.html', {})