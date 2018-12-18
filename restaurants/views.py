from django.shortcuts import render

from .models import RestaurantLocation


def restaurant_list(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'list': queryset
    }
    return render(request, template_name, context)
