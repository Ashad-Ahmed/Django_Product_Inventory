# serializers.py
from rest_framework import serializers
from products.models import Product, Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__' 
    
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory_type = SubCategorySerializer()
    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ['id','description','created','changed']