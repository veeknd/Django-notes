from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import addRecordForm
from django.contrib import messages
from .models import Record
from django.views.generic.list import ListView 
from django.urls import reverse
# Create your views here.
class homeView(ListView):
    model = Record
    template_name = 'home.html'
    context_object_name = 'records'
    
def addRecord(request):
    if request.method== "POST":
        form = addRecordForm(request.POST)

        if form.is_valid():
            add = form.save()
            messages.success(request,"added")
            return HttpResponseRedirect('/')
    else:
        form = addRecordForm()
    return render(request,'addrecord.html',{'form':form})

def viewRecord(request,pk):
    record = Record.objects.get(id=pk)
    cntxt = {'record':record}
    return render(request,'viewRecord.html',cntxt)

def deleteRecord(request,pk):
    Record.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse("home"))

def updateRecord(request,pk):
    current = Record.objects.get(id=pk)
    if request.method == 'POST':
        form = addRecordForm(request.POST, instance=current)
        if form.is_valid():
            update = form.save()
            return redirect(home)
    else:
        form = addRecordForm(instance=current)
    
    return render(request,'updateRecord.html',{'form':form ,'id':pk})
