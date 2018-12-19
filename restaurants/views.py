from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import RestaurantLocation


def restaurant_list(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'list': queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):

    def get_queryset(self):

        search = self.kwargs.get('search')

        if search:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=search) |
                Q(category__icontains=search)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


class RestaurantDetailView(DetailView):
    model = RestaurantLocation

    # # implementation for custom "id" parameter (not pk)
    # def get_object(self, *args, **kwargs):
    #     restaurant_id = self.kwargs.get('id')
    #     restaurant = get_object_or_404(RestaurantLocation, id=restaurant_id)
    #     return restaurant

