from rest_framework import serializers

from app.models import Blog, CategoriasBlogModel, Product, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    
    section = SectionSerializer()
    
    class Meta:
        model = Product
        fields = '__all__'
    

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
class BlogCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasBlogModel
        fields = '__all__'