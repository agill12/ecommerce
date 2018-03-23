from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from decimal import *
from cart.utils import get_cart_items_and_total
from coupon.forms import CouponForm
from django.http import HttpResponse
from coupon.models import Coupon

def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    
    return render(request, "cart/view_cart.html", context)
 
def apply_coupon(request):
   
    if request.method=='POST':
        form=CouponForm(request.POST)
        if form.is_valid():
            if Coupon.objects.filter(code=request.POST['code']).exists():
                cart = request.session.get('cart', {})
                context = get_cart_items_and_total(cart)
                q=Coupon.objects.get(code=request.POST['code'])
                
                total=context['total']
                total=Decimal(total-(total*(q.discount))).quantize(Decimal('.01'))
                cart_items = []
                for item_id, item_quantity in cart.items():
                    this_product = get_object_or_404(Product, pk=item_id)
                    this_total = this_product.price * Decimal(item_quantity)
                    this_item = {
                        'product_id': item_id, 
                        'image': this_product.image,
                        'name': this_product.name,
                        'quantity': item_quantity,
                        'price': this_product.price,
                        'total': this_total,
                    }
                    cart_items.append(this_item)
                    request.session['cart'] = cart  
                # coupon=form.save(commit=False)
                # coupon.save()
                
                return render(request,"cart/view_cart.html",{'cart_items': cart_items,'total': total})
    else:
        form=CouponForm()
    return HttpResponse("cart/view_cart.html",{'form':form})
        
    
    
    
    
    
    
def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('home')



def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')   
    

def update_quantity(request,id):
    quantity = int(request.POST.get('quantity',0))
    cart = request.session.get('cart', {})
    cart[id] =  quantity
    
    request.session['cart'] = cart   

    return redirect('view_cart')

    
    
    
    
    
 