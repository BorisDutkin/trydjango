"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView

from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html')),
    path('login/', LoginView.as_view(), name='login'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('restaurants/create/', RestaurantCreateView.as_view()),
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/search/<slug:search>/', RestaurantListView.as_view()),
    # path('restaurants/<int:id>/', RestaurantDetailView.as_view()), # use custom id
    # path('restaurants/<int:pk>/', RestaurantDetailView.as_view()), # use pk
    path('restaurants/<slug:slug>/', RestaurantDetailView.as_view()),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='contact.html')),
]
