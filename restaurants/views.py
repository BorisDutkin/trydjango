from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurant_create(request):

    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/restaurants')

    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


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


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants'
