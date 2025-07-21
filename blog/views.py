from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
import datetime
from .models import Record
from django.contrib import messages
# Create your views here.
def signup(request):
  if request.method=='POST':
     form=UserCreationForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('login')
  else:
    form=UserCreationForm()
  return render(request,'sign_up.html',{"form":form})
def log_in(request):
  if request.method=="POST":

    form=AuthenticationForm(data=request.POST)

    if form.is_valid():
      login(request,form.get_user())
      return redirect('record1')
  else:
    form=AuthenticationForm()
  return render(request,'login.html',{'form':form})
  
@login_required(login_url='login')
def record1(request):

  record=Record.objects.all().values().order_by('name')
  count=record.count()
  if count==0:
    return   render(request,'record.html',{'count':count,'has_error':True})
  else:
    return   render(request,'record.html',{'record':record,'count':count})

def adds(request):
  time=datetime.datetime.now()
  date=time.strftime('X')
  if request.method=='POST':

    profile=Record()
    profile.name=request.POST['name']
    profile.city=request.POST['city']
    profile.street=request.POST['street']
    
    profile.state=request.POST['state']
    profile.postal_code=request.POST['zipcode']
    profile.id=request.POST['id']
    profile.save()
    return redirect('record1')
  
  else:
    return render(request,'add.html')

def sadik(request,person):
  
  sadik=Record.objects.get(name=person)
  return render(request,'record2.html',{'sadik':sadik})
def deletion(request,names):
  sadik=Record.objects.get(name=names)
  sadik.delete()
  return redirect('record1')
def log_out(request):
    
    logout(request)
    return redirect('login')
def my_view(request):
  # Perform some action, e.g., saving a form 
  messages.success(request, 'Your profile was updated successfully!')
  return redirect('login')