from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    params={'product':product}
    return render(request,"mall/index.html",params)

def about(request):
    return render(request,"mall/about.html")    

def contact(request):
    return render(request,"mall/contact.html")

def prodview(request,id):
    product = Product.objects.filter(id=id)
    return render(request,"mall/product.html",{'product':product[0]})


def cart(request):
    return render(request,"mall/cart.html")    
