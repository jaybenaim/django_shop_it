from django.db import models 
from django.forms import ModelForm 
from django import forms 

class Store(models.Model): 
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    section_id = models.ManyToManyField('Section', related_name='store_sections')


    def __str__(self): 
        return self.name

class Section(models.Model): 
    name = models.CharField(max_length=225)
    aisle_id = models.ManyToManyField('Aisle', related_name='aisles')

    def __str__(self):
        return self.name

class Aisle(models.Model): 
    name = models.CharField(max_length=225)
    shelf_id = models.ManyToManyField('Shelf', related_name="shelves", blank=True)
    
    def __str__(self):
        return self.name

class Shelf(models.Model): 
    shelf_third = models.CharField(max_length=225, default="Front-Third") 
    product_id = models.ManyToManyField('Product', related_name='products') 

    def __str__(self):
        return self.shelf_third

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
   
    def __str__(self): 
        return self.name
        
class User(models.Model): 
    name = models.CharField(max_length=225)
    shopping_list = models.ManyToManyField(Product, related_name='shopping_lists')
    section_order_preference = models.CharField(max_length=225, default="Produce-First")
    store_preference = models.ForeignKey(Store, on_delete=models.CASCADE) 
    budget = models.FloatField()

    def __str__(self):
        return self.name 
