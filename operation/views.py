from django.shortcuts import render,redirect
from.forms import UserRegistration
from .models import User
import requests




# Create your views here.
def addshow(request):
    if request.method=='POST':
        frm=UserRegistration(request.POST)
        if frm.is_valid():
            frm.save()
            frm=UserRegistration() 
    else:
        frm=UserRegistration() 
    name=User.objects.all()
       
    return render(request,'operation/addshow.html',{'form':frm,'users':name})


def delete(request,id):
    if request.method=='POST':
        dele=User.objects.get(pk=id)
        dele.delete()
    return redirect('/zerver/app/addshow')

def update(request,id):
    request.method=='POST'
    gt=User.objects.get(pk=id)
    gte=UserRegistration(request.POST,instance=gt)
    if gte.is_valid():
        gte.save()
        gte=UserRegistration()

    else:
        gt=User.objects.get(pk=id)
        gte=UserRegistration(instance=gt)
    return render(request,'operation/edit.html',{'frm':gte})

def api_ext(request):
    #if request.method=='GET':

      response = requests.get("https://slack.webnyxa.com/api/v1/users")
      sen={'ren':response}
      return render(request,'operation/api.html',context=sen)





