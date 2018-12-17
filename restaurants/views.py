import random
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num'] = None
        context['some_list'] = [
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000)
        ]
        context['condition_bool_item'] = True
        condition_bool_item = True

        if condition_bool_item:
            context['num'] = random.randint(0, 1000000)

        return context