from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import registerform
# Create your views here.

def register(rq):
    if rq.method == 'POST':
        form = registerform(rq.POST)
        if form.is_valid():
            form.save()
        return redirect('/shop/')
    else:
        form = registerform()
        return render(rq, "register/register.html",{"form":form})
