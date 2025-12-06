from django.shortcuts import render
from .models import Brand, Product, Category


def main_page(request):
    brands = Brand.objects.all()
    products = Product.objects.all
    category = Category.objects.all

    context = {'brands': brands, 'products': products, 'category': category}

    return render(request, 'index.html', context)