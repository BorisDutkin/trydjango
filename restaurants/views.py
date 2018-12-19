from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

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
