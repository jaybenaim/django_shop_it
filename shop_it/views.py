from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime 
from shop_it.models import * 
from django import forms 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate
from django.urls import reverse 

def root(request):
    return redirect('home/')

def home(request): 
    stores = Store.objects.all() 
    sections = Section.objects.all() 
    aisles = Aisle.objects.all()
    shelves = Shelf.objects.all()
    products = Product.objects.all()
    users = User.objects.all() 
  
    context = { 
        'stores': stores, 
        'sections': sections, 
        'aisles': aisles,
        'shelves': shelves,
        'products': products,
        'users': users,
    
    }
    return render(request, 'index.html', context) 


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

def signup(request):
    form = UserCreationForm() 
    context =  {'form': form} 
    return render(request, 'registration/signup.html', context)


def signup_create(request): 
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
        new_user = form.save()
        login(request, new_user)
        return redirect('/')
    else: 
        return render(request, 'registration/signup.html', {'form': form})
