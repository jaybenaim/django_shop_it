from django.db import models 
from django.forms import ModelForm 
from shop_it.models import *

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['name', 'shopping_list', 'section_order_preference', 'store_preference']

class ProductForm(ModelForm): 

    class Meta: 
        model = Product 
        fields = ['name', 'price']

class ShelfForm(ModelForm): 

    class Meta: 
        model = Shelf 
        fields = ['shelf-third', 'product_id']


class AisleForm(ModelForm): 

    class Meta: 
        model = Aisle 
        fields = ['name', 'shelf_id']

class SectionForm(ModelForm): 

    class Meta: 
        model = Section 
        fields = ['name', 'aisle_id']


class StoreForm(ModelForm): 

    class Meta: 
        model = Store
        fields = ['name', 'address', 'section_id']

