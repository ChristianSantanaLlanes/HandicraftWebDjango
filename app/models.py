from distutils.text_file import TextFile
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Section(models.Model):
    name = models.CharField('Nombre', max_length=30)
    description = models.TextField('Descripcion')
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=50)
    description = models.TextField('Descripcion')
    price = models.FloatField('Precio')
    en_venta = models.BooleanField('En Venta', default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
    def section_name(self):
        return self.section.name
    
    def __str__(self):
        return self.name
    
class ImagenProducto(models.Model):
    imagen = models.CharField('Imagen', help_text='Debe subir la imagen a un servidor y copiar la ruta aqui', max_length=100, null=True)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='imagenes')
    
    def __str__(self):
        return self.imagen
    
    
class CategoriasBlogModel(models.Model):
    name = models.CharField('Nombre', max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    category = models.ForeignKey(CategoriasBlogModel, on_delete=models.CASCADE)
    name = models.CharField('Titulo', max_length=50)
    description = models.TextField('Descripcion')
    content = RichTextField(blank=True, null=True)
    created = models.DateTimeField('Creado', auto_now=True, auto_created=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    position = models.CharField('Posicion del texto', max_length=10, choices=(('isquierda', 'Isquierda'), ('derecha', 'Derecha')) ,default='derecha')
    imagen = models.CharField('Imagen', help_text='Use un bot de telegram de imgur para subir las fotos y copie el enlace aqui', max_length=100, null=True)
    
    class Meta:
        ordering = ['-created']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)
    
    def category_name(self):
        return self.category.name
    
    def __str__(self):
        return self.name
    