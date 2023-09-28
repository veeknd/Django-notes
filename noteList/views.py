from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import addRecordForm
from django.contrib import messages
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    return render(request,"home.html",{'records':records})

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

def deleteRecord(self,pk):
    Record.objects.filter(id=pk).delete()
    return redirect(home)

