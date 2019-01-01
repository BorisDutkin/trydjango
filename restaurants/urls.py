from django.urls import path

from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

app_name = 'restaurants'

urlpatterns = [
    path('create/', RestaurantCreateView.as_view(), name='create'),
    path('', RestaurantListView.as_view(), name='list'),
    path('search/<slug:search>/', RestaurantListView.as_view(), name='search'),
    # path('restaurants/<int:id>/', RestaurantDetailView.as_view()), # use custom id
    # path('restaurants/<int:pk>/', RestaurantDetailView.as_view()), # use pk
    path('<slug:slug>/', RestaurantDetailView.as_view(), name='detail')
]
