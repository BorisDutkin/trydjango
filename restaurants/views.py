import random
from django.shortcuts import render
from django.views import View


# function based view
def home(request):

    num = None

    some_list = [
        random.randint(0, 1000000),
        random.randint(0, 1000000),
        random.randint(0, 1000000)
    ]

    condition_bool_item = True

    if condition_bool_item:
        num = random.randint(0, 1000000)

    return render(request, 'home.html', {
        'num': num,
        'some_list': some_list
    })


def about(request):

    num = None

    some_list = [
        random.randint(0, 1000000),
        random.randint(0, 1000000),
        random.randint(0, 1000000)
    ]

    condition_bool_item = True

    if condition_bool_item:
        num = random.randint(0, 1000000)

    return render(request, 'about.html', {
        'num': num,
        'some_list': some_list
    })


def contact(request):

    num = None

    some_list = [
        random.randint(0, 1000000),
        random.randint(0, 1000000),
        random.randint(0, 1000000)
    ]

    condition_bool_item = True

    if condition_bool_item:
        num = random.randint(0, 1000000)

    return render(request, 'contact.html', {
        'num': num,
        'some_list': some_list
    })


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'contact.html', context)

    # def post(self, request, *args, **kwargs):
    #     context = {}
    #     return render(request, 'contact.html', context)
    #
    # def put(self, request, *args, **kwargs):
    #     context = {}
    #     return render(request, 'contact.html', context)


