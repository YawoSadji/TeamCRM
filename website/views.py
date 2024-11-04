from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Record
from .forms import RecordForm
from django.http import HttpResponse
import csv
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
    
def export_to_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition']='attachment; filename="contacts.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Address', 'City', 'State', 'Zipcode'])
    records = Record.objects.all()
    for record in records:
        writer.writerow([record.id, record.first_name, record.last_name, record.email, record.phone, record.address, record.city, record.state, record.zipcode])
    return response

@login_required
def search_record(request):
    if request.method == "POST":
        search = request.POST['search']
        results = Record.objects.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search),
            user=request.user
            )
        return render(request, 'search.html', {'search': search, 'results':results})
    else:
        return redirect('loggedIn')


def logout_user(request):
    logout(request)
    return render(request, 'home.html', {})