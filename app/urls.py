from django.urls import include, path, re_path

from app.views import IndexPage, ProductPage


urlpatterns = [
    path('', IndexPage.as_view(),name='home'),
    path('product/', ProductPage.as_view(),name='product'),
]
