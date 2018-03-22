from django.shortcuts import render,get_object_or_404,redirect
from products.models import Product
from .forms import NewProductsForm
from reviews.forms import ReviewForm

# Create your views here.
def new_product(request):
    if request.method=='POST':
        form=NewProductsForm(request.POST,request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.save()
            return redirect('home')
    else:
        form=NewProductsForm()
    return render(request, 'products/products.html',{'form':form})
    
def view_product(request,id):
    products = get_object_or_404(Product, pk=id)
    form = ReviewForm()
    return render(request, "products/view_product.html", {'products': products, 'review_form': form })
    
def product_list(request):
    products = Product.objects.all
    return render(request,"products/product_list.html",{'products':products} )
