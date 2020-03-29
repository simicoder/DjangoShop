from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from store.models import *


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user.is_active = True
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def home_view(request, category=None):
    if category is None:
        queryset = Product.objects.all()
    else:
        category = get_object_or_404(Category, name=category)
        queryset = Product.objects.filter(category=category)

    categories = Category.objects.all()

    context = {
        'products': queryset,
        'categories': categories
    }

    return render(request, 'store/home.html', context)


def create_view(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, 'store/createProduct.html', context)


def info_view(request):
    return render(request, 'store/info.html')


def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'store/product_view.html', context)


def account_info_view(request):
    return render(request, 'store/account.html')