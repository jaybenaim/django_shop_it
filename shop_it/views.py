from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from shop_it.models import * 
from django import forms 

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

