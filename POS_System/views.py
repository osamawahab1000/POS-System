from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()

    dicto = {'products': products}

    return render(request, 'POS_System/index.html', dicto)
