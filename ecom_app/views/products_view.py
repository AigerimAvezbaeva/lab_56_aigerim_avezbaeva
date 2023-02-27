from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from ecom_app.models import Product
from ecom_app.forms import ProductForm


def add_product(request: WSGIRequest):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add_product.html', context={
        'form': form
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', context={
        'product': product
    })


def update_product(request, pk):
    errors = {}
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if not request.POST.get('name'):
            errors['title'] = 'Данное поле обязательно к заполнению'
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.quantity = request.POST.get('quantity')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        if errors:
            return render(request, 'update_product.html', context={
                'product': product,
                'form': form,
                'errors': errors
            })
        form.save()
        return redirect('index')
    return render(request, 'update_product.html', context={
        'product': product,
        'form': form
    })


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'confirm_delete.html', context={
        'product': product
    })


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')
