from django.shortcuts import render,redirect
from .forms import VoterForm
from .models import Voter

# Create your views here.
def vview(request):
    form = VoterForm()
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/voter.html",{"form":form})

def sview(request):
    obj = Voter.objects.all()
    return render(request,"app1/show.html",{"obj":obj})
def hview(request):
    return render(request,"app1/home.html",{})


def uview(request,pk):
    obj= Voter.objects.get(vid=pk)
    form = VoterForm(instance=obj)
    if request.method == "POST":
        form = VoterForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/voter.html",{"form":form})

def dview(request,k):
    obj = Voter.objects.get(vid=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})