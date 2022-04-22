# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subcategory_name

class Category(models.Model):

    category_name = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(max_length=200 , blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    subcategory_type = models.ForeignKey(SubCategory , blank=True, null=True , on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
