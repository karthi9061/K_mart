from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    f_products=Product.objects.order_by('priority')[:4]
    L_products=Product.objects.order_by('-id')[:4]
    context={'f_products':f_products, 'L_products':L_products}
    return render(request, 'index.html',context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    Product_list=Product.objects.order_by('priority')
    product_paginators=Paginator(Product_list,2)
    Product_list=product_paginators.get_page(page)
    context={'products': Product_list}
    return render(request, 'products.html', context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product': product}
    
    return render(request, 'products_detail.html',context)