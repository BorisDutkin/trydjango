from django.urls import path


from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemUpdateView,
    ItemListView
)

app_name = 'menus'

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail')
]
