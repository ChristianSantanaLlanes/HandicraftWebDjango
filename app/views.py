from django.shortcuts import render
from django.views import generic
from rest_framework.response import Response
from rest_framework import viewsets, generics
from app.models import Blog, CategoriasBlogModel, Product, Section

from app.serializers import BlogCategoriaSerializer, BlogSerializer, ProductSerializer, SectionSerializer

# Create your views here.

class IndexPage(generic.TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Section.objects.all()
        context["productos"] = Product.objects.all()
        return context
    
    
class ProductPage(generic.DetailView):
    template_name = 'product.html'
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Section.objects.all()
        return context
    
def search_section(request, id):
    
    categorias = Section.objects.all()
    if id != 'all':
        queryset = Product.objects.filter(section=id)
        section = Section.objects.get(id=id)
    else:
        queryset = Product.objects.all()
        section = {'name':'Todos los Productos'}
    
    return render(request, 'listing.html', {'products':queryset, 'section':section, 'categorias':categorias})

class BlogView(generic.TemplateView):
    template_name = 'blog_posts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Section.objects.all()
        context["sections"] = CategoriasBlogModel.objects.all()
        context["last_post"] = Blog.objects.all()[:4]
        context["blogs"] = Blog.objects.all()
        posts = Blog.objects.all()
        i = 0
        for post in posts:
            i = i+1
            if i%2:
                post.position = 'derecha'
            else:
                post.position = 'isquierda'
        return context
    
class BlogDetailView(generic.DetailView):
    template_name = 'blog_post_single.html'
    model = Blog
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = CategoriasBlogModel.objects.all()
        context["last_post"] = Blog.objects.all()[:4]
        return context
    
    
class ProductRestApi(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()
    
class SectionRestApi(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = SectionSerializer.Meta.model.objects.all()
    
class BlogRestApi(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = BlogSerializer.Meta.model.objects.all().order_by('-created')[:3]
    
class BlogCategoriaRestApi(viewsets.ModelViewSet):
    serializer_class = BlogCategoriaSerializer
    queryset = BlogCategoriaSerializer.Meta.model.objects.all().order_by('name')