from django.shortcuts import render, redirect
from django.views import generic
from app.models import Section

from car.models import Car

# Create your views here.

# def car_view(request):
#     categorias = Section.objects.all()
#     if request.user.is_authenticated:
#         user = request.user
#         queryset = Car.objects.get(user=user)
#         return render(request, 'shopping_cart.html', {'productos':queryset,'sections':categorias})
#     else:
#         return redirect('login')