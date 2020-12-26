"""storemanagementsystem URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from stockmanagement.views import homeview, list_item, add_item, update_item, delete_item,\
    details_view,issue_item,receive_item,reorder_level


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homeview, name='home'),
    # path('$', homeview,name='home'),
    path('list/', list_item, name='list'),
    path('add/', add_item, name='add'),
    path('update/<str:pk>/', update_item, name='update'),
    path('delete/<str:pk>/', delete_item, name='delete'),
    path('detail/<str:pk>/', details_view, name='detail'),
    path('issue/<str:pk>/', issue_item, name='issue'),
    path('receive/<str:pk>/', receive_item, name='receive'),
    path('reorder_level/<str:pk>/', reorder_level, name='reorder_level'),
    # path('accounts/', include('registration.backends.default.urls')),


]
