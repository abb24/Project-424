from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Phone
from PhoneStore.forms import SignUpForm



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return reverse()
    else:
        form = SignUpForm()

    return render(request, 'PhoneStore/register.html', {'form': form})
    

def logina(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # replace 'home'with the name of your home page URL pattern
        else:
            # handle invalid login credentials
            pass
    else:
        return render(request, 'PhoneStore/login.html')
    



def phone(request, phone):
    phone = phone.objects.get(phone = phone)
    context = { 'phone': phone }
    return render(request, 'PhoneStore/allProducts.html' , context )
    



class NewItemForm(forms.Form):
    item = forms.IntegerField(label='Number of items')



def index(request):

    if "PhoneStore" not in request.session:

        request.session["PhoneStore"] = []

    return render(request, "PhoneStore/index.html" , {"PhoneStore": request.session["PhoneStore"]})

def add(request):
    if request.method == "POST":
        form=NewItemForm(request.POST)

        if form.is_valid():

            item=form.cleaned_data["item"]

            request.session["PhoneStore"]+=[item]

            return HttpResponseRedirect(reverse("PhoneStore:index"))
        else:
            return render(request, "PhoneStore/add.html" , {})

    return render(request, "PhoneStore/add.html" , {"form": NewItemForm()})





