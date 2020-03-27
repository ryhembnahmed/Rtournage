from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import Formulaire

from Rtournage.models import Product, Category, Transaction


# Create your views here.


def index(request):
    all_product = Product.objects.all()
    all_category = Category.objects.all()
    dictionnary = {
        'all_product': all_product,
        'all_category': all_category
    }
    return render(request, 'Rtournage/index.html', dictionnary)


def add_prod(request):
    cat_id = request.POST.get('cat_id')
    type = request.POST.get('type')
    ref = request.POST.get('ref')
    quantity = request.POST.get('quantity')
    min = request.POST.get('min')
    max = request.POST.get('max')
    my_cat = Category.objects.get(pk=cat_id)
    existing_prods = Product.objects.filter(category=my_cat, type=str(type), reference=str(ref))
    if existing_prods.__len__() == 0:
        prod = Product(type=str(type), reference=str(ref), quantity=quantity, min_limit_alert=min, max_limit_alert=max,
                       category=my_cat)
        prod.save()
    return HttpResponseRedirect(reverse('Rtournage:index', args=()))


def del_prod(request, id):
    product = Product.objects.get(pk=id)
    if product.transactions.all().__len__() != 0:
        data = {'status': 'error'}
    else:
        product.delete()
        data = {'status': 'success'}
    return JsonResponse(data, safe=False)


def statistic(request):
    return render(request, 'Rtournage/statistic.html')


def category(request):
    all_category = Category.objects.all()
    return render(request, 'Rtournage/category.html', {'all_category': all_category})


def add_cat(request):
    name = request.POST.get('name')
    existing_cat = Category.objects.filter(name=name)
    if existing_cat.__len__() == 0:
        cat = Category(name=name)
        cat.save()
    return HttpResponseRedirect(reverse('Rtournage:category', args=()))


def edit_cat(request):
    name = request.POST.get('name')
    id = request.POST.get('id')
    existing_cat = Category.objects.filter(name=name)
    if existing_cat.__len__() == 0:
        cat = Category(id=id, name=name)
        cat.save()
    return HttpResponseRedirect(reverse('Rtournage:category', args=()))


def del_cat(request, id):
    category = Category.objects.get(pk=id)
    if category.products.all().__len__() != 0:
        data = {'status': 'error'}
    else:
        category.delete()
        data = {'status': 'success'}
    return JsonResponse(data, safe=False)


def del_buy(request, id):
    buy_transaction = Transaction.objects.get(pk=id)
    if buy_transaction.type == 1:
        buy_transaction.product.quantity -= buy_transaction.quantity
        buy_transaction.product.save()
        buy_transaction.delete()
        data = {'status': 'success'}
    else:
        data = {'status': 'error'}
    return JsonResponse(data, safe=False)


def del_sell(request, id):
    sell_transaction = Transaction.objects.get(pk=id)
    if sell_transaction.type == 2:
        sell_transaction.product.quantity += sell_transaction.quantity
        sell_transaction.product.save()
        sell_transaction.delete()
        data = {'status': 'success'}
    else:
        data = {'status': 'error'}

    return JsonResponse(data, safe=False)


def add_buy(request):
    prod_id = request.POST.get('prod_id')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    date = request.POST.get('date')
    product = Product.objects.get(pk=prod_id)
    trans_buy = Transaction(product=product, quantity=quantity, price=price, date=date, type=1)
    trans_buy.save()

    return HttpResponseRedirect(reverse('Rtournage:buy', args=()))


def add_sell(request):
    prod_id = request.POST.get('prod_id')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    date = request.POST.get('date')
    product = Product.objects.get(pk=prod_id)
    trans_buy = Transaction(product=product, quantity=quantity, price=price, date=date, type=2)
    trans_buy.save()

    return HttpResponseRedirect(reverse('Rtournage:sell', args=()))


def buy(request):
    all_buy = Transaction.objects.filter(type=1).order_by('-date')
    products = Product.objects.all()
    dictionnary = {
        'all_buy': all_buy,
        'products': products,
    }
    return render(request, 'Rtournage/buy.html', dictionnary)


def sell(request):
    all_sell = Transaction.objects.filter(type=2).order_by('-date')
    products = Product.objects.all()
    dictionnary = {
        'all_sell': all_sell,
        'products': products,
    }
    return render(request, 'Rtournage/sell.html', dictionnary)


def edit_prod(request):
    prod_id = request.POST.get('prod_id')
    cat_id = request.POST.get('cat_id')
    type = request.POST.get('type')
    ref = request.POST.get('ref')
    quantity = request.POST.get('quantity')
    min = request.POST.get('min')
    max = request.POST.get('max')
    my_cat = Category.objects.get(pk=cat_id)
    existing_prods = Product.objects.filter(category=my_cat, type=str(type), reference=str(ref))
    if existing_prods.__len__() == 0:
        prod = Product(id=prod_id, type=str(type), reference=str(ref), quantity=quantity, min_limit_alert=min,
                       max_limit_alert=max,
                       category=my_cat)
        prod.save()
    return HttpResponseRedirect(reverse('Rtournage:index', args=()))
