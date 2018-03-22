"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from home.views import get_index
from django.views.static import serve
from django.conf import settings
from accounts import urls as accounts_urls
from products import urls as products_urls
from cart import urls as cart_urls
from reviews import urls as urls_reviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='home'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^cart/',include(cart_urls)),
    url(r'^reviews/', include(urls_reviews)),
    
    
    
]
