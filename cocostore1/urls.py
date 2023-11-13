"""cocostore1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bag.views import bag
from home.views import homepage, contact, about
from shop.views import detail_product, detail_categories

urlpatterns = [
    path('', homepage, name='homepage'),
    path('bag/', bag, name='bag'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('<slug:category_slug>/<slug:slug>/', detail_product, name='detail_product'),
    path('<slug:slug>/', detail_categories, name='detail_categories'),
]
