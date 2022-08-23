from django.urls import include, path, re_path
from rest_framework import routers
from app.views import BlogCategoriaRestApi, BlogDetailView, BlogRestApi, BlogView, IndexPage, ProductPage, ProductRestApi, SectionRestApi, search_section

router = routers.DefaultRouter()
router.register(r'productos', viewset=ProductRestApi)
router.register(r'secciones', viewset=SectionRestApi)
router.register(r'blogs', viewset=BlogRestApi)
router.register(r'categoria', viewset=BlogCategoriaRestApi)

urlpatterns = [
    path('', IndexPage.as_view(),name='home'),
    path('product/<slug:slug>/', ProductPage.as_view(),name='product'),
    path('list/products/<id>/', search_section,name='list-product'),
    path('list/blogs/', BlogView.as_view(),name='blogs'),
    path('list/blogs/<str:slug>/', BlogDetailView.as_view(),name='blogs-detail'),
    path('api/v1/', include(router.urls), name='api'),
]