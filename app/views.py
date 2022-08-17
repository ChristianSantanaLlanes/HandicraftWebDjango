from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexPage(generic.TemplateView):
    template_name = 'index.html'
    
class ProductPage(generic.TemplateView):
    template_name = 'product.html'