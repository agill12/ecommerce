from django.conf.urls import url,include


from .views import *


urlpatterns = [
    url(r'^new_product', new_product, name="new_product"),
    url(r'^view_product/(\d+)', view_product, name="view_product"),
    url(r'^product_list', product_list, name="product_list"),
  
     
   
    
    ]
    
    