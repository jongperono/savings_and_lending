"""SLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from apps import views

urlpatterns = [
    path('', views.home, name='home'),
    path('savings/list/', views.savings_list, name='savings_list'),
    path('savings/add/', views.savings_add, name='savings_add'),

    path('savings/person/(?<id>[^/]+)/$', views.savings_person, name='savings_person'),
    
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
