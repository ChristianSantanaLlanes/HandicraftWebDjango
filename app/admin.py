from django.contrib import admin

from app.models import Blog, CategoriasBlogModel, ImagenProducto, Product, Section

# Register your models here.

class ImagenProductAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_editable = ['price']
    search_fields = ['name']
    list_filter = ['section']
    inlines = [ImagenProductAdmin]
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'created']
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Section)
admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(CategoriasBlogModel)